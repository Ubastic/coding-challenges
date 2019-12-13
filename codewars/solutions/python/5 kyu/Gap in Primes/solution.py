from math import sqrt
from itertools import count, islice


def primes(start, end):
    def is_prime(n):
        return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))

    yield from (i for i in range(start, end) if is_prime(i))


def gap(g, m, n):
    gen = primes(m, n)
    first = next(gen)

    for i in gen:
        first, second = i, first
        if first - second == g:
            return [second, first]