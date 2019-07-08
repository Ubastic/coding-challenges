from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def primes(start, end):
    yield from (i for i in range(start, end) if is_prime(i))


def step(g, m, n):
    for i in primes(m, n):
        for j in primes(i + g, n):
            if j - i > g:
                break

            if j - i == g:
                return [i, j]
