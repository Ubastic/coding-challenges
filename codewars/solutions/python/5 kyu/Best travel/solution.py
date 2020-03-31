from itertools import combinations


def choose_best_sum(t, k, ls):
    return min(filter(lambda i: i <= t, map(sum, combinations(ls, k))), key=lambda c: t - c, default=None)