def exchange_with(a, b):
    a[:], b[:] = b[::-1], a[::-1]