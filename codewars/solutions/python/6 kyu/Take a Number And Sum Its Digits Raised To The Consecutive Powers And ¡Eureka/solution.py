def sum_dig_pow(a, b):
    return [i for i in range(a, b + 1) if i == sum(int(n) ** p for p, n in enumerate(str(i), 1))]
