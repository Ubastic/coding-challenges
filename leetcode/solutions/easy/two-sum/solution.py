class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapped = {}
        for i, n in enumerate(nums):
            j = target - n
            if j in mapped:
                return [mapped[j], i]
            mapped[n] = i