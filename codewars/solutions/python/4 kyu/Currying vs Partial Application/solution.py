def curry_partial(f, *initial_args):
    if not callable(f):
        return f
    for i in reversed(range(len(initial_args) + 1)):
        try:
            return f(*initial_args[:i])
        except TypeError: pass
    return lambda *args: curry_partial(f, *(initial_args + args))
