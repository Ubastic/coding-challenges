def gen(l):
    for i in l:
        try:
            yield from i
        except TypeError:
            yield i

def flatten(lst):
    return list(gen(lst))