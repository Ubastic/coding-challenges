from math import sqrt
from itertools import count, islice

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
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

@memoize
def check_num(n):
    return not is_prime(n) and all(is_prime(int(i)) for i in str(n))

def not_primes(a, b):
    return [i for i in range(a,b) if check_num(i)]