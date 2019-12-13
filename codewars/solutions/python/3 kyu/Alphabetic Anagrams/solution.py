from collections import Counter
from math import factorial
from operator import mul
from functools import reduce


def listPosition(word):
    frq = {**Counter(word)}
    alp_arr = sorted(set(word))

    w, t = '', 1
    while w != word:
        for alp in alp_arr:
            if frq[alp] > 0:
                cur = w + alp
                if word.startswith(cur):
                    frq[alp] -= 1
                    w += alp
                    break
                else:
                    t += factorial(len(word) - len(cur)) // reduce(
                        mul, (factorial(v - (k == alp)) for k, v in frq.items()), 1
                    )

    return t
