class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cache = set()

        for n in nums:
            if n in cache:
                cache.remove(n)
            else:
                cache.add(n)

        res, = cache
        return res