from itertools import groupby


def alphabetized(s):
    return ''.join(''.join(i) for _, i in groupby(sorted(filter(str.isalpha, s), key=str.lower), str.lower))
