class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        for n in reversed(nums):
            if not n:
                zeros += 1
                nums.remove(n)

        nums.extend([0] * zeros)