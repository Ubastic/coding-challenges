from itertools import cycle, chain
from collections import Counter

def iter_over(string, n):
    return zip(string, cycle(chain(range(n), reversed(range(1, n - 1)))))

def encode_rail_fence_cipher(string, n):
    return string if n == 1 or not string else ''.join(i for i, _ in sorted(iter_over(string, n), key=lambda a: a[1]))

def decode_rail_fence_cipher(string, n):
    if n == 1 or not string:
        return string

    values = [*Counter(i for _, i in iter_over(string, n)).values()]
    arr = [[*string[sum(values[:i]): sum(values[: i + 1])]] for i in range(len(values))]
    return ''.join(arr[i].pop(0) for _, i in iter_over(string, n))