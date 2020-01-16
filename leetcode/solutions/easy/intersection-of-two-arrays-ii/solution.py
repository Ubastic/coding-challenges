class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        
        for n in nums1:
            try:
                nums2.remove(n)
                intersection.append(n)
            except ValueError:
                pass
        
        return intersection
            