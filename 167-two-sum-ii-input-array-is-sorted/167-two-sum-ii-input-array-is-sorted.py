class Solution:
    def twoSum(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            if nums[lo] + nums[hi] == target:
                break
            elif nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                lo += 1
        return [lo + 1, hi + 1]