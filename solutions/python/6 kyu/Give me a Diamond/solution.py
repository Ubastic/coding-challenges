from math import ceil


def diamond(n):
    if n <= 0 or n % 2 == 0:
        return None

    n = ceil(n / 2)
    l = [" " * (n - i) + "*" * (i * 2 - 1) for i in range(1, n + 1)]
    return '\n'.join(l + l[:-1][::-1]) + '\n'

