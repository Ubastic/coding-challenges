from math import gcd
from functools import reduce


def convertFracts(lst):
    if not lst:
        return lst

    res = reduce(lambda a, b: a * b // gcd(a, b), (i for _, i in lst))
    return [[res // j * i, res] for i, j in lst]