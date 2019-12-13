class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        s = str(x)
        return all(s[i] == s[- (i + 1)] for i in range(len(s) // 2)) or len(s) == 1
