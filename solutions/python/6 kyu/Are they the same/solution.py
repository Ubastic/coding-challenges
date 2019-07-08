def comp(a, b):
    return a is not None and b is not None and all(i ** 2 == j for i, j in zip(sorted(a), sorted(b)))
