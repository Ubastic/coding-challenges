from functools import partial

ROMAN = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}


def solution(n):
    res, str_n = '', str(n)
    for c, p in zip(map(int, str_n), map(partial(pow, 10), range(len(str_n))[::-1])):
        if (c + 1) % 5 == 0:
            res += ROMAN[p]
            c += 1

        res += ROMAN.get(c * p) or (ROMAN[5 * p] + ROMAN[p] * (c - 5) if c > 5 else ROMAN[p] * c)

    return res
