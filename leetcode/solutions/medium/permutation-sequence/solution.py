import math


def get_permutation(arr: List[int], k: int) -> str:
    if len(arr) == 1:
        return str(arr[0])

    index, reminder = divmod(k, math.factorial(len(arr) - 1))
    return ''.join(str(i) for i in [arr.pop(index), *get_permutation(arr, reminder)])


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return get_permutation([i + 1 for i in range(n)], k - 1)
