class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stats = Counter(nums)
        nums[:] = [*([0] * stats[0]), *([1] * stats[1]), *([2] * stats[2]),]