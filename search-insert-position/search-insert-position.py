class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi, mid = 0, len(nums) - 1, 0
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return mid if target < nums[mid] else mid + 1
        