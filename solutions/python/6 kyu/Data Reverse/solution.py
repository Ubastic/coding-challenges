from itertools import chain


def data_reverse(l):
    return [*chain.from_iterable(l[i * 8: (i + 1) * 8] for i in reversed(range(len(l) // 8)))]
