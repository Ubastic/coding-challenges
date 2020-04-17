def memoize(func):
    cache = {}
    def wrapper(p, n):
        key = tuple(p), n
        if key not in cache:
            cache[key] = func(p, n)
        return cache[key]
    return wrapper

@memoize
def cut_log(p, n):
    if (n == 0):
        return 0
    q = -1
    for i in range(1, n+1):
        q = max(q, p[i] + cut_log(p, n-i))

    return q