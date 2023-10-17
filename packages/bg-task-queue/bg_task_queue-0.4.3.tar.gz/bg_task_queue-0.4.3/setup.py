
from setuptools import setup, find_packages

setup(
    name='bg_task_queue',
    version='0.4.3',
    package_dir={"": "src"},
    py_modules=["src/__init__", "src/bg_task_queue"],
    install_requires=[],
    license='MIT',
    author="jhleee",
    author_email="ng0301@gmail.com",
    description="python simple multi threading task queue",
    url="https://github.com/jhleee/python-bg-task-queue",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)


