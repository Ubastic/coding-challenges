import sys

sys.setrecursionlimit(2 ** 31 - 1)


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]

        r = cache[args] = func(*args)
        return r

    return wrapper


@memoize
def exp_sum(n, k=None):
    if k is None:
        k = n

    if 0 < k <= n:
        return exp_sum(n, k - 1) + exp_sum(n - k, k)
    elif k > n:
        return exp_sum(n, n)
    elif n == 0 and k == 0:
        return 1
    else:
        return 0
