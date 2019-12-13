def generator(n: str):
    for i in range(len(n)):
        for j in range(len(n)):
            l = [*n]
            l.insert(j, l.pop(i))
            yield [int(''.join(l).lstrip('0')), i, j]


def smallest(n):
    return min(generator(str(n)))