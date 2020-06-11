class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        return re.match(".*" + "".join(f"{c}.*" for c in s), t) is not None
