# Background Task Queue

## Overview

## Installation

```bash
pip install bg-task-queue
```

## Example

```python
import time
from src.bg_task_queue import BackgroundTaskQueue

tq = BackgroundTaskQueue(verbose=True, max_workers=2)


# add function using decorator
@tq.function
def task_a(i):
    time.sleep(1)
    print(f'Task_a({i}) Finished')


# or add manually
def task_b(a=0):
    time.sleep(3)
    print(f'Task_b({a}) Finished')


tq.function(task_b)

tq.add_task("task_a", 100)
tq.add_task("task_b", a=200)
tq.add_task("task_a", 300)
tq.add_task("task_a", 400)

while True:
    summary = {"pending": 0, "running": 0, "stopped": 0, "errored": 0, "success": 0}
    tasks = tq.get_all_tasks()
    for t in tq.get_all_tasks():
        print(t)
        summary[t.status] += 1
    print(summary)
```

```text
...
[*] Worker-1 : End 71f323e7-5b25-4870-b22d-667dda0c5749
[*] Worker-1 : takes job 3472f262-8a7d-446c-a601-fb5a02284f22
[*] Worker-1 : Start 3472f262-8a7d-446c-a601-fb5a02284f22
<Task id=71f323e7-5b25-4870-b22d-667dda0c5749, status=success function=task_a, args=[100], kwargs={}>
<Task id=8220b58b-3087-43d2-a813-cd2c0c8458e0, status=running function=task_b, args=[], kwargs={"a": 200}>
<Task id=3472f262-8a7d-446c-a601-fb5a02284f22, status=running function=task_a, args=[300], kwargs={}>
<Task id=6c7c27fc-ccc5-419b-8b92-61b5738dfa51, status=pending function=task_a, args=[400], kwargs={}>
{'pending': 1, 'running': 2, 'stopped': 0, 'errored': 0, 'success': 1}
...
```


## Classes

### `Status` (Enum)

- **PENDING**: The task is pending execution.
- **RUNNING**: The task is currently running.
- **SUCCESS**: The task successfully completed.
- **ERROR**: The task ran into an error during execution.
- **STOPPED**: The task has been stopped.

### `Task`

- `id`: Unique identifier for the task.
- `func_name`: The name of the function to run.
- `args`: Positional arguments for the function.
- `kwargs`: Keyword arguments for the function.
- `status`: The current status of the task. Default is `PENDING`.

### `BackgroundTaskQueue`

- `db_path`: Database path for SQLite3. Default is `:memory:`.
- `max_workers`: Maximum number of worker threads. Default is `2`.
- `verbose`: Enables verbose logging. Default is `False`.
- `falling_rate`: The sleep time between each worker loop. Default is `0.1`.


## License
This project is licensed under the MIT License. See LICENSE.md for more details.