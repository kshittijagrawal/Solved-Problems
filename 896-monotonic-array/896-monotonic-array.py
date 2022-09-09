class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag, i = None, 1
        while i < len(nums) and nums[i] == nums[i-1]: i += 1
        while i < len(nums):
            if not flag:
                flag = 1 if nums[i] > nums[i-1] else -1
            if flag > 0 and not nums[i] >= nums[i-1]: return False
            if flag < 0 and not nums[i] <= nums[i-1]: return False
            i += 1
        return True