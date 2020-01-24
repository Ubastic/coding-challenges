import numpy as np
from collections import Counter
from itertools import chain


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        array = np.array(board)
        array_t = array.T
        digits = {*map(str, range(10)), '.'}

        for l in chain(
                array,
                array_t,
                (
                        array[i * 3: (i + 1) * 3, j * 3: (j + 1) * 3].flatten()
                        for i in range(3) for j in range(3)
                )
        ):
            if (
                    not {*l}.issubset(digits)
                    or {*Counter(i for i in l if i != '.').values()} not in ({1}, set())
            ):
                return False

        return True