import numpy as np


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        array = np.rot90(np.array(matrix), -1)
        for i in range(len(array)):
            matrix[i] = [*map(int, array[i])]
