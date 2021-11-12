class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ind = m + n - 1
        m, n = m - 1, n - 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[ind] = nums1[m]
                m -= 1
            else:
                nums1[ind] = nums2[n]
                n -= 1
            ind -= 1
        
        while n >= 0:
            nums1[ind] = nums2[n]
            ind, n = ind - 1, n - 1