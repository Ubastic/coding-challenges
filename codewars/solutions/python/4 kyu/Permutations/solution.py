from itertools import permutations as per

def permutations(string):
    return list(set(map(''.join, per(string))))
