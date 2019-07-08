from itertools import chain

import numpy
import math


class Sudoku:
    def __init__(self, data):
        self.data = data
        self.size = len(data)

    def is_valid(self):
        if any(len(a) != self.size for a in self.data) or any(type(i) != int for i in chain(*self.data)):
            return False

        digits = set(range(1, self.size + 1))
        board = numpy.array(self.data)

        if not (all(set(a) == digits for a in board) and all(set(a) == digits for a in board.T)):
            return False

        root = int(math.sqrt(self.size))

        for i in range(root):
            for j in range(root):
                if board[i * root:(i + 1) * root, j * root:(j + 1) * root].sum() != sum(digits):
                    return False
        return True
