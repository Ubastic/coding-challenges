from itertools import groupby


def find_outlier(integers):
    return next(i[0] for i in (list(a) for _, a in groupby(sorted(integers, key=lambda a: a % 2), key=lambda a: a % 2)) if len(i) == 1)
