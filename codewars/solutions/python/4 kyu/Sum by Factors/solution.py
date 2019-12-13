from math import sqrt
from itertools import count, islice


def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def sum_for_list(lst):
    return [
        [a, sum(b)] for a, b in
        ([i, [j for j in lst if j % i == 0]] for i in range(abs(max(lst, key=abs)) + 1) if is_prime(i)) if b
    ]