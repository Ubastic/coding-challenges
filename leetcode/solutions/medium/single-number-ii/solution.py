class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        double_seen = set()

        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                double_seen.add(n)

        res, = seen - double_seen
        return res
            