from itertools import permutations


def slogan_maker(array):
    return [' '.join(p) for p in permutations([a for i, a in enumerate(array) if array.index(a) == i])]
