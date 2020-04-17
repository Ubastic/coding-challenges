import _thread
import time

canary = object()


def handle(func, success, failure, *exceptions):
    return_value = exception_value = canary

    def _inner():
        nonlocal return_value, exception_value

        try:
            return_value = func()
        except Exception as e:
            exception_value = e

    _thread.start_new_thread(_inner, (), {})

    while return_value is canary and exception_value is canary:
        time.sleep(0.01)

    if return_value is not canary:
        success(func, return_value)
    elif isinstance(exception_value, exceptions):
        failure(func, exception_value)
    else:
        raise exception_value