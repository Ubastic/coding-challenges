from collections import Counter


def score(dice):
    c = Counter(dice)
    s = 0
    for i in range(1, 7):
        if c[i] >= 3:
            s += 1000 if i == 1 else i * 100
            c[i] -= 3

    return s + c[1] * 100 + c[5] * 50