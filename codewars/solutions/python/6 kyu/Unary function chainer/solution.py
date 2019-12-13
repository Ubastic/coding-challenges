def chained(functions):
    return lambda a: reduce(lambda i, f: f(i), functions, a)
