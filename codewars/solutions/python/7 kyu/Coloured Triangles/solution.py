values = ['R', 'G', 'B']


def new_colour(a, b):
    if a == b:
        return a

    return values[3 - values.index(a) - values.index(b)]


def triangle(row):
    while len(row) != 1:
        row = ''.join(new_colour(a, b) for a, b in zip(row, row[1:]))

    return row
