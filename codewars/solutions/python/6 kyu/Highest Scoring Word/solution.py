def high(x):
    return max(x.split(), key=lambda c: sum(ord(i) - ord('a') + 1 for i in c))
