class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi, res = 0, len(nums)-1, float("inf")
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] < res:
                res = nums[mid]
            if nums[lo] <= nums[mid]:
                if nums[mid] <= nums[hi]: hi = mid - 1
                else: lo = mid + 1
            else:
                hi = mid - 1
        return res