class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        return lo if target <= nums[lo] else lo + 1