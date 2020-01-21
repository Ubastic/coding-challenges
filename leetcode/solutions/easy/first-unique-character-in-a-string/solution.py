class Solution:
    def firstUniqChar(self, s: str) -> int:
        checked = set()
        for i, c in enumerate(s):
            if c not in checked and c not in s[i+1:]:
                return i
            checked.add(c)
        return -1