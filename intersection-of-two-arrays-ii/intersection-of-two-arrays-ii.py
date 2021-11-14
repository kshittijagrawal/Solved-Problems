class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1) < len(nums2): nums1, nums2 = nums2, nums1
        c = collections.Counter(nums1)
        
        for i in range(len(nums2)):
            if c.get(nums2[i], 0):
                res.append(nums2[i])
                c[nums2[i]] -= 1
        
        return res