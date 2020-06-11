class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return next((i for i, n in enumerate(nums) if n >= target), len(nums))