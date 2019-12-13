from re import search


def triple_double(n1, n2):
    n1, n2 = str(n1), str(n2)
    return any(search(c + '{3}', n1) and search(c + '{2}', n2) for c in set(n1))