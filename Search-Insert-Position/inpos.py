class Solution:
    def searchInsert(self, nums, target):
        lo, mid, hi = 0, 0, len(nums)-1
        while lo<hi:
            mid = lo + ((hi-lo)//2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        if target > nums[mid]:
            return mid+1
        return mid
        