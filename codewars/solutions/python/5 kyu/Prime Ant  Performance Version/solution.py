import math
from itertools import count, islice

cache = {}


def is_prime(n):
    if n not in cache:
        for number in islice(count(2), int(math.sqrt(n) - 1)):
            if not n % number:
                cache[n] = number
                return number

        cache[n] = -1
        return -1

    return cache[n]


def prime_ant(n):
    pos = 0
    arr = [2]
    len_arr = 1
    steps = 0

    while steps < n:
        q = is_prime(arr[pos])

        if q == -1:
            pos += 1

            if len_arr == pos:
                arr.append(len_arr + 2)
                len_arr += 1

        else:
            arr[pos - 1] += q
            arr[pos] /= q

            pos -= 1

        steps += 1

    return arr[:pos + 1]