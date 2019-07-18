import sys


def count_calls(func, *args, **kwargs):
    calls = -1

    def trace(*args, **kwargs):
        nonlocal calls
        calls += 1

    sys.settrace(trace)
    rv = func(*args, **kwargs)
    return calls, rv