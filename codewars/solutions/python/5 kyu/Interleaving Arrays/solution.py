from itertools import zip_longest, chain


def interleave(*args):
    return [*chain(*zip_longest(*args))]