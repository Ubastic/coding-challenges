from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))


def sum_primes(lower, upper):
    return sum(filter(is_prime, xrange(lower, upper + 1))) if upper >= lower else 0