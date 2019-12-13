from contextlib import suppress
from itertools import chain

from numpy import matrix


def check(field, col):
    field, res = matrix([f + [' '] * (6 - len(f)) for f in field]).A, col * 4

    def get_dialog(i, j, mul=1):
        with suppress(IndexError):
            return ''.join(field[i + o][(j + (o * mul)) if (j + (o * mul)) >= 0 else len(field[i])] for o in range(4))

    return any((any(res in ''.join(f) for f in a) for a in (field, field.T))) or \
           any(chain.from_iterable(((get_dialog(i, j) == res or get_dialog(i, j, -1) == res
                                     for j in range(len(field[i]))) for i in range(len(field)))))


def who_is_winner(pieces_position_list):
    field = [[] for _ in 'ABCDEFG']
    for c, col in map(lambda s: s.split('_'), pieces_position_list):
        field['ABCDEFG'.index(c)].append(col[0].lower())
        if check(field, col[0].lower()):
            return col
    return "Draw"