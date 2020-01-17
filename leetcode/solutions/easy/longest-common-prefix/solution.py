class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = []
        for s in zip(*strs):
            if s.count(s[0]) == len(s):
                common.append(s[0])
            else:
                break

        return ''.join(common)