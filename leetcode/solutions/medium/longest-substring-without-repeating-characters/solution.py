class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = set()
        pos = max_size = 0

        while True:
            for c in s[pos:]:
                if c in arr:
                    max_size = max(len(arr), max_size)
                    pos += 1
                    arr.clear()
                    break
                else:
                    arr.add(c)
            else:
                return max(len(arr), max_size)