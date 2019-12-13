from collections import Counter, defaultdict
from itertools import chain


def mix(s1, s2):
    c1 = Counter(c for c in s1 if c.islower() and s1.count(c) > 1)
    c2 = Counter(c for c in s2 if c.islower() and s2.count(c) > 1)

    d = defaultdict(lambda: defaultdict(list))
    for k in {*c1, *c2}:
        a, b = c1[k], c2[k]
        key = k * max(a, b)
        if a == b:
            d[len(key)][0].append((key, '='))
        elif a > b:
            d[len(key)][1].append((key, '1'))
        else:
            d[len(key)][2].append((key, '2'))

    def sort(it):
        return sorted(it, key=lambda a: a[0])

    return '/'.join(
        f'{j}:{i}' for i, j in
        chain(*(chain(sort(d[i][1]), sort(d[i][2]), sort(d[i][0])) for i in sorted(d, reverse=True)))
    )
