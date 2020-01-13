class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = None
        for n in reversed(nums):
            if n == x:
                nums.remove(x)
            x = n

        return len(nums)