from typing import List
from itertools import islice, chain


def sorted_arr(a: List[int], b: List[int]):
    while a and b:
        yield a.pop(0) if a[0] < b[0] else b.pop(0)
    yield from chain(a, b)


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        index = (total_len - 1) // 2

        if total_len % 2:
            return sum(islice(sorted_arr(nums1, nums2), index, index + 1))
        else:
            return sum(islice(sorted_arr(nums1, nums2), index, index + 2)) / 2