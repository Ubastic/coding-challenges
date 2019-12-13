from itertools import islice, count
import math


def memoize(func):
    cache = {}
    def wrapp(n):
        res = cache.get(n)
        if res is None:
            res = func(n)
            cache[n] = res
        return res
    return wrapp


@memoize
def is_prime(n):
    for number in islice(count(2), int(math.sqrt(n) - 1)):
        if not n % number:
            return False

    return True


def total(arr):
    return sum(a for i, a in enumerate(arr[2:], 2) if is_prime(i))
