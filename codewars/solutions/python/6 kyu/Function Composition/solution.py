def compose(f,g):
    return lambda *args, **kwargs: f(g(*args, **kwargs))