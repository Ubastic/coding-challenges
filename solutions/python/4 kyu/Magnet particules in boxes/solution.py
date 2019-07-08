def memoize(func):
    cache = {}

    def wrapper(*args):
        # print(f'{func.__name__}: {args!r}')
        if args in cache:
            return cache[args]
        result = cache[args] = func(*args)
        return result

    return wrapper


@memoize
def u(k, N):
    base, power = 1 / k, 2 * k

    return sum(base * (1 / ((n + 1) ** power)) for n in range(1, N + 1))


def doubles(K, N):
    return sum(u(k, N) for k in range(1, K + 1))
