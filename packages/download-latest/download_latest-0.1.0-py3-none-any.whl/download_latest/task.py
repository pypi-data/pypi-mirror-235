from __future__ import annotations

import subprocess
import threading
from typing import ClassVar, Generic, Iterable, Sequence, TypeVar
import time

__all__ = [
    "NOT_SET",
    "NOT_SET_TYPE",
    "SubProcessTask",
    "Task",
    "TaskException",
    "TaskTimeout",
    "TaskUncaughtError",
]


# Sentinel class
class NOT_SET_TYPE:
    pass


# Sentinel
NOT_SET = NOT_SET_TYPE()

# Generic Type
T = TypeVar("T")


class TaskException(Exception):
    """Exception for Task."""

    pass


class TaskTimeout(TaskException):
    """Exception for Task.get() / Task.wait() when timeout is specified."""

    def __init__(self, timeout: float | int) -> None:
        super().__init__(f"{timeout}s elapsed")
        self.timeout = timeout


class TaskUncaughtError(TaskException):
    """Exception indicating that the task ended with an uncaught exception."""

    def __init__(self, error: Exception) -> None:
        super().__init__(repr(error))
        self.error = error


class Task(Generic[T]):
    """
    A concurrent task runner using threading.Thread.

    Example:

    >>> class DivideTask(Task[float]):
    ...     def __init__(self, a: int, b: int) -> None:
    ...         super().__init__()
    ...         self.a, self.b = a, b
    ...
    ...     def run(self) -> float:
    ...         time.sleep(0.1)
    ...         return float(self.a / self.b)
    ...
    >>> task = DivideTask(1, 2)
    >>> task.get()
    0.5
    >>> task = DivideTask(1, 0)
    >>> task.get()
    Traceback (most recent call last):
        ...
    task.TaskUncaughtError: ZeroDivisionError('division by zero')
    >>> task = DivideTask(1, 4)
    >>> for i in task.loop(period=0.04):
    ...     print(i)
    0
    1
    2
    >>> task.get()
    0.25
    """

    MAX_SLEEP: ClassVar[float] = 1 / 60

    _error: Exception | None
    _ready: threading.Event
    _result: T | NOT_SET_TYPE
    _thread: threading.Thread | None

    def __init__(self) -> None:
        """
        Create the task.
        """
        self._error = None
        self._ready = threading.Event()
        self._result = NOT_SET
        self._thread = None

    def get(self, timeout: float | int | None = None) -> T:
        """
        Return the task's result.

        If the task wasn't already started, it will be started.

        If timeout is specified, then block at most timeout seconds. If the task
        hasn't finished, then raise a TaskTimeout exception.

        If timeout is not specified, then block until the task finishes.

        If the task ends or ended with an uncaught exception, then raise a
        TaskUncaughtError.
        """
        self.start()

        if not self._ready.wait(timeout):
            raise TaskTimeout(timeout or 0)
        if self._error:
            raise TaskUncaughtError(self._error)
        elif isinstance(self._result, NOT_SET_TYPE):  # pragma: no cover
            raise TaskException("unexpected result state")
        else:
            return self._result

    def loop(self, period: float | int | None = None) -> Iterable[int]:
        """
        Return an iterator of integers starting at 0, ending when the task
        finishes.

        If period is specified, this will not iterate more than once every
        period seconds.

        This is guaranteed to iterate at least once, even if the task has
        finished before the loop starts.

        If the task ends or ended with an uncaught exception, then raise a
        TaskUncaughtError.
        """
        index = 0
        period_time = period if period is not None and period > 0 else 0
        start_time = time.time()

        self.start()

        while index == 0 or self.running():
            yield index
            index += 1
            while True:
                wait_time = (period_time * index) + start_time - time.time()
                if wait_time <= 0 or not self.running():
                    break
                time.sleep(min(wait_time, self.MAX_SLEEP))

    def run(self) -> T:
        """
        The main activity run by a separate thread. Subclasses should override
        this method.
        """
        raise NotImplementedError()  # pragma: no cover

    def running(self) -> bool:
        """
        Return whether or not the task is running.
        """
        return bool(self._thread) and not self._ready.is_set()

    def start(self) -> None:
        """
        Start the task if it hasn't already been started.
        """
        if not self._thread:

            def target() -> None:
                # We're not going to worry about BaseExceptions
                try:
                    self._result = self.run()
                except Exception as e:
                    self._error = e
                finally:
                    self._ready.set()

            self._thread = threading.Thread(target=target, daemon=True)
            self._thread.start()

    def wait(self, timeout: float | int | None = None) -> None:
        """
        Wait for the task to finish.

        Has the arguments and functionality as get() except it doesn't return
        anything.
        """
        self.get(timeout)


class SubProcessTask(Task[subprocess.CompletedProcess]):
    """
    A concurrent subprocess runner.

    Example:

    >>> task = SubProcessTask("sleep 1; echo -n done")
    >>> task.get().stdout
    b'done'
    """

    def __init__(self, args: Sequence[str] | str | bytes):
        """
        Create a subprocess Task.
        """
        super().__init__()
        self.args = args

    def run(self) -> subprocess.CompletedProcess:
        """
        Run a subprocess of args and return a CompletedProcess.
        """
        return subprocess.run(
            self.args,
            capture_output=True,
            shell=isinstance(self.args, (str, bytes)),
        )
