import time
from functools import wraps
from typing import Any


def stop_watch(function: Any) -> Any:
    """
    A decorator that measures and prints the execution time of a function.

    This decorator records the start and end times when the specified function is called.
    Upon completion of the function execution, the elapsed time (in seconds) is printed to the standard output.
    This decorator is useful for performance analysis or debugging to understand the execution time of a function.

    Parameters:
    function (Any): The function whose execution time you want to measure.

    Returns:
    Any: The return value of the wrapped function.

    Usage:
    @stop_watch
    def sample_function():
        # Some process

    sample_function()  # Execution time will be printed
    """

    @wraps(function)
    def wrapper(*args: Any, **kargs: Any) -> Any:
        start = time.time()
        result = function(*args, **kargs)
        elapsed_time = time.time() - start
        print(f"{function.__name__}: {elapsed_time}")
        return result

    return wrapper
