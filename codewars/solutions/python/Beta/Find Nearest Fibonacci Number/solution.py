from math import log

LOG_5 = log(5) / 2
LOG_PI = log((1 + 5 ** 0.5) / 2)


def memoize(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return wrapper


@memoize
def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 1 else n


def nearest_fibonacci(n):
    if not n:
        return 0

    y = int((log(n) + LOG_5) / LOG_PI)
    return min(fib(y), fib(y + 1), key=lambda i: abs(n - i))