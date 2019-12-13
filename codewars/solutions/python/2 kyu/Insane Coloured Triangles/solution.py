def triangle(row):
    rev = {'R': 1, 'G': 2, 'B': 3}

    def derive(x, y):
        if x == y:
            return x

        return ' RGB'[rev[x] ^ rev[y]]

    while len(row) > 1:
        step = 1
        while step * 3 < len(row):
            step *= 3

        row = [derive(v, row[i + step]) for i, v in enumerate(row[:-step])]

    return row[0]
