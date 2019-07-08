"""
If you watch at my solution it contains two parts:

1. Stolen code to check that number is prime (
    I took it from original solution, from solution.py file, some kind of hack :)
).

2. Function that iterates over number and find all that meed expectation.


If was trying to speed-up my implementation of is_prime function, my implementation is:

>>> @memoize
... def is_prime(n):
...    if n < 2 or not n & 1:
...        return False
...
...    for x in range(3, int(sqrt(n)) + 1, 2):
...       if not n % x:
...           return False
...
...    return True

I memize all calculated numbers, but this implementation took many time to check that number is prime.

So if you read this comments, please:
Help me to speed-up my implementation or explain how works stolen code.

Contact point: 1998uriyyo@gmail.com
"""
# Begin of stolen code
from random import randint


def decompose(n):
    e = 0

    while n % 2 == 0:
        n >>= 1
        e += 1

    return e, n


def is_witness(possible_witness, p, exponent, remainder):
    possible_witness = pow(possible_witness, remainder, p)
    if possible_witness in (1, p - 1):
        return False

    for _ in range(exponent):
        possible_witness = pow(possible_witness, 2, p)

        if possible_witness == p - 1:
            return False

    return True


def is_prime(p, accuracy=100):
    if p < 2:
        return False
    elif p in (2, 3):
        return True

    exponent, remainder = decompose(p - 1)

    return not any(is_witness(randint(2, p - 2), p, exponent, remainder) for _ in range(accuracy))


# Begin of my code
def convert(n):
    """
    If n ends on odd number then return n otherwise return zero
    """
    return n if ord(n[-1]) % 2 else 0


def predicate(n):
    """
    Check that reversed square n and cube n are prime numbers
    """
    return is_prime(int(convert(str(n ** 2)[::-1]))) and is_prime(int(convert(str(n ** 3)[::-1])))


def solution():
    # Memoize all calculated results to avoid recalculation
    result = {}

    # Every call of wrapper starts from:
    i = 88  # Current iterated number
    c = 0  # Index of last calculated number

    def wrapper(n):
        # Check if n already calculated
        if n in result:
            return result[n]

        # Use closure to start from last position
        nonlocal i, c

        # Calculate sequence numbers
        while c < n:
            # Check that number meet expectations
            if predicate(i):
                # Save calculated result and return found value
                c += 1
                result[c] = i

            i += 1

        return i - 1

    return wrapper


sq_cub_rev_prime = solution()
