import math


def divisor_generator(n):
    for i in filter(lambda a: n % a == 0, range(1, int(math.sqrt(n) + 1))):
        yield from (i, *((n / i,) if i * i != n else ()))


def predicate(i):
    s = int(sum(j ** 2 for j in divisor_generator(i)))
    return [i, s] if math.sqrt(s) % 1 == 0 else None


def list_squared(m, n):
    return [i for i in (predicate(j) for j in range(m, n)) if i]
