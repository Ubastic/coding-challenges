import math

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(math.ceil(len(s) / 2)):
            s[i], s[-(i + 1)] = s[-(i + 1)], s[i]