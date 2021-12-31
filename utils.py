import time


def get_execution_time(function, *args, **kwargs):
    start_time = time.time()
    function(*args, **kwargs)
    end_time = time.time()
    return round(end_time - start_time, 6)
