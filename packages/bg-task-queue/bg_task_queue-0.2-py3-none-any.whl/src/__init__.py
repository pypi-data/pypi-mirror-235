import ctypes
import json
import sqlite3
import sys
import threading
import time
import uuid
from enum import Enum


class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    ERROR = "error"
    STOPPED = "stopped"


class Task:
    def __init__(self, _id, func_name, status=Status.PENDING, args=None, kwargs=None):
        self.id = _id
        self.func_name = func_name
        self.args = args
        self.kwargs = kwargs
        self.status = status

    def __str__(self):
        return f"<Task id={self.id}, status={self.status} function={self.func_name}, args={self.args}, kwargs={self.kwargs}>"

    __repr__ = __str__


class TerminateException(SystemExit):
    pass


def _terminate_thread(thread):
    print(f"[*] terminating thread {thread.name}")
    if not thread.is_alive():
        return
    exc = ctypes.py_object(SystemExit)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
        ctypes.c_long(thread.ident), exc)
    if res == 0:
        raise ValueError("Invalid thread ID")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread.ident, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
    return True


# noinspection SqlNoDataSourceInspection
class BackgroundTaskQueue:
    def __init__(self, db_path=":memory:", max_worker=2, verbose=False, falling_rate=0.1):
        self.verbose = verbose
        self.__db_lock = threading.Lock()
        self._worker_mange_lock = threading.Lock()
        self.__conn = sqlite3.connect(db_path, check_same_thread=False)
        BackgroundTaskQueue._create_tables(self.__conn)
        self._functions = {}
        self._max_worker = max_worker
        self._workers = []
        self.falling_rate = falling_rate

        if verbose:
            print(f"[*] Starting background task queue")
            print(f"[*] workers: {max_worker}")

        for i in range(max_worker):
            worker = threading.Thread(target=self.__worker, args=[i], daemon=True)
            worker.name = f"worker-{i}"
            worker.start()
            self._workers.append((str(i), worker))

    @property
    def max_worker(self):
        return self._max_worker

    @max_worker.setter
    def max_worker(self, value):
        new_worker_count = value - self._max_worker
        self._max_worker = value
        if self.verbose:
            print(f"[*] set max worker: {self._max_worker}")
        for i in range(new_worker_count):
            self._add_worker()

    @property
    def live_thread(self):
        return sum([thread.is_alive() for i, thread in self._workers])

    def function(self, func, name=None):
        if name is None:
            name = func.__name__
        self._add_function(name, func)

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    def push_task(self, func_name, *args, **kwargs):
        task_id = str(uuid.uuid4())
        serialized_args = json.dumps(args)
        serialized_kwargs = json.dumps(kwargs)
        with self.__db_lock, self.__conn:
            self.__conn.execute("INSERT INTO tasks (id, func_name, args, kwargs) VALUES (?, ?, ?, ?)",
                              (task_id, func_name, serialized_args, serialized_kwargs))
            if self.verbose:
                print(f"[*] Adding task [{task_id}] {func_name}")
        return Task(task_id, func_name, args=args, kwargs=kwargs)

    def stop_task(self, task_id):
        with self.__db_lock, self.__conn:
            cursor = self.__conn.cursor()
            cursor.execute("BEGIN IMMEDIATE")
            task = cursor.execute("SELECT id, worker_id FROM tasks WHERE id = ?", (task_id,)).fetchone()
            if task:
                _, worker_id = task
                worker = self._get_worker(worker_id)
                if worker:
                    if self.verbose:
                        print(f"[*] Stopping task {task_id}, worker {worker_id} ({worker.native_id})")
                    try:
                        self._restart_worker(worker_id)
                        cursor.execute("UPDATE tasks SET status ='stopped' WHERE id = ?", (task_id,))
                        if self.verbose:
                            print(f"[*] Stopped task {task_id}")
                    except Exception as e:
                        print(f"[*] Error while terminating worker {worker_id}: {e}", file=sys.stderr)
            cursor.execute("COMMIT")
        self.__conn.commit()

    def get_task(self, task_id):
        with self.__db_lock, self.__conn:
            task = self.__conn.execute("SELECT id, func_name, worker_id, status, args, kwargs "
                                     "FROM tasks WHERE id =?", (task_id,)).fetchone()
            if task:
                return Task(task_id, func_name=task[1], status=task[2], args=task[3], kwargs=task[4])
            return None

    def get_tasks(self, state=None):
        with self.__db_lock, self.__conn:
            tasks = []
            if state:
                states = state.split("|")
                placeholders = ', '.join('?' for _ in states)
                sql = f"SELECT id, func_name, worker_id, status, args, kwargs " \
                      f"FROM tasks WHERE status IN ({placeholders})"
                results = self.__conn.execute(sql, states).fetchall()
            else:
                results = self.__conn.execute("SELECT id, func_name, worker_id, status, args, kwargs "
                                            "FROM tasks").fetchall()

            for [task_id, func_name, _, status, args, kwargs] in results:
                tasks.append(Task(task_id, func_name, status=status, args=args, kwargs=kwargs))
            return tasks

    @staticmethod
    def _create_tables(conn):
        with conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id TEXT PRIMARY KEY,
                    worker_id TEXT,
                    func_name TEXT,
                    args TEXT,
                    kwargs TEXT,
                    status TEXT DEFAULT 'pending',
                    result TEXT
                )
            """)

    def _add_function(self, func_name, func):
        if func_name in self._functions:
            raise Exception(f"[*] Function {func_name} already exists")

        self._functions[func_name] = func

        if self.verbose:
            print(f"[*] Adding function {func_name}")

    def _add_worker(self):
        with self._worker_mange_lock:
            if self.live_thread >= self._max_worker:
                print(f"[*] Worker limit reached ({self._max_worker})", file=sys.stderr)
                return

            worker_id = str(uuid.uuid4())
            new_worker = threading.Thread(target=self._worker, args=[worker_id], daemon=True)
            new_worker.name = f"worker-{worker_id}"
            new_worker.start()
            if self.verbose:
                print(f"[*] Restart worker {worker_id} ({new_worker.native_id})")
            return new_worker

    def _get_worker(self, worker_id):
        for i, worker in self._workers:
            if i == worker_id:
                return worker

    def _restart_worker(self, worker_id):
        worker = None
        for w in self._workers:
            if worker_id == w[0]:
                worker = w
                break
        if not worker:
            print(f"[*] Worker {worker_id} not found", file=sys.stderr)
            raise Exception(f"Worker {worker_id} not found")

        self._workers.remove(worker)
        worker_id, thread = worker
        with self._worker_mange_lock:
            _terminate_thread(thread)
            new_worker = self._add_worker()
        if self.verbose:
            print(f"[*] Restart worker {worker_id} ({new_worker.native_id})")
        self._workers.append((worker[0], new_worker))

    def __worker(self, worker_id):
        while True:
            with self._worker_mange_lock:
                if self.live_thread >= self._max_worker:
                    if self.verbose:
                        print(
                            f"[*] Worker-{worker_id} : Stopping. Because {self.live_thread}/{self._max_worker} workers are alive",
                            file=sys.stderr)
                    break
            with self.__db_lock, self.__conn:
                cursor = self.__conn.cursor()
                task = cursor.execute(
                    "SELECT id, func_name, args, kwargs FROM tasks WHERE status = 'pending' LIMIT 1").fetchone()
                if task:
                    task_id, func_name, serialized_args, serialized_kwargs = task
                    if self.verbose:
                        print(f"[*] Worker-{worker_id} : takes job {task_id}")
                    cursor.execute("UPDATE tasks SET status = 'running', worker_id = ? WHERE id = ?",
                                   (str(worker_id), task_id))
                self.__conn.commit()

            if task:
                task_id, func_name, serialized_args, serialized_kwargs = task
                args = json.loads(serialized_args)
                kwargs = json.loads(serialized_kwargs)
                with self.__conn:
                    try:
                        func = self._functions[func_name]

                        if self.verbose:
                            print(f"[*] Worker-{worker_id} : Start {task_id}")

                        result = func(*args, **kwargs)
                        result = json.dumps(result)

                        if self.verbose:
                            print(f"[*] Worker-{worker_id} : End {task_id}")

                        self.__conn.execute("UPDATE tasks SET status = 'success', result = ? WHERE id = ?",
                                          (result, task_id))
                    except Exception as e:
                        print(f"[*] Worker-{worker_id} : {func_name}, {str(args)}, {str(kwargs)} {str(e)}",
                              file=sys.stderr)
                        self.__conn.execute("UPDATE tasks SET status = 'error', result = ? WHERE id = ?",
                                          (str(e), task_id))
            time.sleep(self.falling_rate)
