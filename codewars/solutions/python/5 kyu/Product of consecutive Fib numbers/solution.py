def productFib(prod):
    i, j = 0, 1
    while True:
        i, j = j, i + j
        if i * j == prod:
            return [i, j, True]
        elif i * j > prod:
            return [i, j, False]
