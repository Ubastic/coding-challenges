from math import gcd
from functools import reduce


def has_subpattern(s):
    return reduce(gcd, map(s.count, {*s})) != 1
