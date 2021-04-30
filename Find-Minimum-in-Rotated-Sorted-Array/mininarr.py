class Solution:
    def findMin(self, nums):
        lo, hi, _min = 0, len(nums)-1, float("inf")
        while lo <= hi:
            mid = lo + ((hi-lo)//2)
            if nums[mid] < _min:
                _min = nums[mid]
            elif nums[mid] >= nums[lo]:
                if nums[lo] <= nums[mid] <= nums[hi]:
                    hi = mid-1
                    continue
                lo = mid+1
            else:
                if nums[lo] <= nums[mid] <= nums[hi]:
                    lo = mid+1
                    continue
                hi = mid-1
        return _min