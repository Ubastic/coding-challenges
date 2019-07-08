def zeros(n):
    zero_count = 0
    power = 5

    while n >= power:
        zero_count += n // power
        power *= 5

    return zero_count
