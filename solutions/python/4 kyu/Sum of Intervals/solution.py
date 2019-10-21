from itertools import chain


def sum_of_intervals(intervals):
    return len(set(chain.from_iterable(range(i, j) for i, j in intervals)))
