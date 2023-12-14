from time import perf_counter
from typing import Callable


def get_execution_time(function: Callable, *args, **kwargs) -> float:
    start_time: float = perf_counter()
    function(*args, **kwargs)
    end_time: float = perf_counter()
    return round(end_time - start_time, 6)
