class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        data = 0

        for i in nums:
            shift = 1 << i

            if data & shift:
                return i

            data |= shift
