from collections import Counter, defaultdict
from operator import mul


def solution(arr):
    data = defaultdict(int, Counter(arr))
    
    while len(data) != 1:
        min_val = min(data)
        
        for k in (a for a in set(data) if a != min_val):
            r = k / min_val
            data[k - min_val * (int(r) - (not r % 1))] += data.pop(k)

    return mul(*next(iter(data.items())))