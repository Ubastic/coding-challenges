import math


def count_bits(col, n):
    d = (n + 1) / (2 << col)
    s = math.floor(d)
    r = max(0, (d - s) * (2 << col) - (1 << col))

    return s * (1 << col) + r


def count_bits_sum(n):
    return sum(count_bits(i, n) for i in range(60))


def countOnes(left, right):
    return int(count_bits_sum(right) - count_bits_sum(left - 1))
