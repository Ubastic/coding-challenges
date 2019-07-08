def fusc(n):
    a, b = 1, 0

    for i in bin(n)[2:]:
        if i == '1':
            b += a
        else:
            a += b

    return b
