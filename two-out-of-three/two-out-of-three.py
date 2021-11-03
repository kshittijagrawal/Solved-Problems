class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        res = [s for s in s1 if s in s2 or s in s3]
        for s in s2:
            if s in s3 and s not in s1:
                res.append(s)
        return res