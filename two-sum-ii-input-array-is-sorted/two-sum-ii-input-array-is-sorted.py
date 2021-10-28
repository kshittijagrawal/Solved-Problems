class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            s = nums[lo] + nums[hi]
            if s == target:
                return [lo+1, hi+1]
            elif s < target:
                lo += 1
            else:
                hi -= 1