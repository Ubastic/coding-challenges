from itertools import cycle

def make_looper(s):
    return lambda i=cycle(s): next(i)