import re

INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

NUMBER = re.compile(r'^[+-]?\d+')

class Solution:
    def myAtoi(self, s: str) -> int:
        match = NUMBER.search(s.strip())
        
        if not match:
            return 0

        return max(min(int(match.group()), INT_MAX), INT_MIN)