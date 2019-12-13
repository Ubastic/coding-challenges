class Solution:
    def reverse(self, x: int) -> int:
        n = abs(int(str(x)[::-1].lstrip('0').rstrip('-') or '0')) * (-1) ** (x < 0)
        return n if -2147483648 <= n <= 2147483647 else 0
