class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = 0
        while x or y:
            x, f = divmod(x, 2)
            y, s = divmod(y, 2)
            diff += f != s
            
        return diff
        