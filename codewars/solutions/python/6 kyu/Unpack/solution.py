from itertools import chain


def unpack(l):
    if isinstance(l, dict):
        return unpack([*chain(*l.items())])
    elif isinstance(l, (int, str, type(None))):
        return [l]
    return [*chain(*map(unpack, l))]