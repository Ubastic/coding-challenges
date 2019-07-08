def persistence(n, t=0):
    n = str(n)
    if len(n) == 1:
        return t
    return persistence(reduce(lambda a, b: int(a) * int(b), n), t + 1)