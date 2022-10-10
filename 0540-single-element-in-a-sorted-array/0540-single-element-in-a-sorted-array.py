class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo)//2
            if mid % 2: # mid is odd
                if nums[mid] == nums[mid - 1]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else: # mid is even
                if nums[mid] == nums[mid + 1]:
                    lo = mid + 2
                else:
                    hi = mid
        return nums[lo]