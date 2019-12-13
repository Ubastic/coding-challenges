def sequence_sum(a1, an, d):
    if a1 > an and d > 0 or a1 < an and d < 0:
        return 0

    n = (an - a1) // d + 1

    return (2 * a1 + d * (n - 1)) * n // 2