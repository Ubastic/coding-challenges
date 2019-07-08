def parse(data):
    arr = []
    i = 0

    for c in data:
        if c == 'i':
            i += 1
        elif c == 'd':
            i += -1
        elif c == 's':
            i *= i
        elif c == 'o':
            arr.append(i)

    return arr