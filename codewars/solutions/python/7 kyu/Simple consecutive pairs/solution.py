def pairs(ar):
    return sum(abs(abs(a) - abs(b)) == 1 for a, b in zip(ar[::2], ar[1::2]))
