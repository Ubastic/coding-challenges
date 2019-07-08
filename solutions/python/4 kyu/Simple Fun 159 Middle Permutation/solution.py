from math import factorial


def middle_permutation(s):
    index = factorial(len(s)) // 2 - 1
    seqc, result = sorted(s), []
    fact = factorial(len(s))
    index %= fact

    while seqc:
        fact = fact // len(seqc)
        choice, index = index // fact, index % fact
        result += [seqc.pop(choice)]

    return ''.join(result)