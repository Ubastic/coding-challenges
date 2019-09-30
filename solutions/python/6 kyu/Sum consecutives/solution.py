from itertools import groupby


def sum_consecutives(array):
    return [sum(i) for _, i in groupby(array)]
