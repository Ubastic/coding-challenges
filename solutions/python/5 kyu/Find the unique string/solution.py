from collections import defaultdict


def find_uniq(arr):
    d = defaultdict(list)
    for i in arr:
        key = frozenset(i.lower().strip())
        d[key].append(i)
        if len(d) > 1:
            res = [v for v in d.values() if len(v) == 1]
            if len(res) == 1:
                return res[0][0]
