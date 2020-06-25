def permute(nums: List[int]):
    if len(nums) == 1:
        yield nums
    else:
        for i, n in enumerate(nums):
            rest = nums[:i] + nums[i + 1:]

            for sub in permute(rest):
                yield [n, *sub]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [*permute(nums)]