from math import factorial, sqrt
from itertools import count, takewhile, islice


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def prime_gen():
    yield from filter(is_prime, count(2))


def conv(f, i):
    n = 0

    while True:
        f, o = divmod(f, i)
        if o:
            break
        n += 1

    return f'^{n}' if n != 1 else ''


def decomp(n):
    f = factorial(n)
    return ' * '.join(f'{i}{conv(f, i)}' for i in takewhile(lambda j: j <= n, prime_gen()))
