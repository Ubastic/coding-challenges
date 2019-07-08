def dig_pow(number, p):
    s = sum(int(n) ** i for i, n in enumerate(str(number), p))

    return -1 if s % number != 0 else s / number