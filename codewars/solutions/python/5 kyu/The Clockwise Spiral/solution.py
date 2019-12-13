def spiral(m, n, s=0):
    if n:
        yield range(s, m + s)
        yield from zip(*[*spiral(n - 1, m, m + s)][::-1])


def create_spiral(m):
    return [[i + 1 for i in a] for a in spiral(m, m)]  if isinstance(m, int) else ''