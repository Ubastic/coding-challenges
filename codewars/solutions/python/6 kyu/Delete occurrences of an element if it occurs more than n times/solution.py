from collections import defaultdict


def delete_nth(order, max_e):
    data = defaultdict(int)
    res = []
    for i in order:
        data[i] += 1
        if data[i] <= max_e:
            res.append(i)

    return res
