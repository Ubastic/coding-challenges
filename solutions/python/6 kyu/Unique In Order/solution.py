from itertools import groupby

def unique_in_order(iterable):
    return [a for a, _ in groupby(iterable)]
