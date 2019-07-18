def uniq(iterable):
    values = set()
    for i in iterable:
        v = tuple(sorted(i))
        if v not in values:
            yield i
            values.add(v)


def memoize(func):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return inner


@memoize
def combos(n):
    if n == 1:
        return [[1]]

    result = [[n]]
    for i in range(1, n):
        result.extend([i] + l for l in combos(n - i))

    return list(uniq(result))
