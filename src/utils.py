import time
from functools import wraps
from typing import Any


def stop_watch(function: Any) -> Any:
    @wraps(function)
    def wrapper(*args: Any, **kargs: Any) -> Any:
        start = time.time()
        result = function(*args, **kargs)
        elapsed_time = time.time() - start
        print(f"{function.__name__}: {elapsed_time}")
        return result

    return wrapper
