class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mindex, nindex = m-1, n-1
        index = m+n-1
        
        while mindex >= 0 and nindex >= 0:
            if nums1[mindex] >= nums2[nindex]:
                nums1[index] = nums1[mindex]
                mindex, index = mindex-1, index-1
            else:
                nums1[index] = nums2[nindex]
                nindex, index = nindex-1, index-1
                
        while nindex >= 0:
            nums1[index] = nums2[nindex]
            nindex, index = nindex-1, index-1