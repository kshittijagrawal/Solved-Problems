class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi  - lo) // 2
            if not mid % 2: # even
                if nums[mid + 1] == nums[mid]:
                    lo = mid + 2
                else:
                    hi = mid
            else: # odd
                if nums[mid - 1] == nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid
        return nums[lo]