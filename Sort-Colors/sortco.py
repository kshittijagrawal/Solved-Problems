class Solution:
    def sortColors(self, nums):
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[curr] = nums[curr], nums[i]
                curr += 1
        curr1 = curr
        for i in range(curr1, len(nums)):
            if nums[i] == 1:
                nums[i], nums[curr] = nums[curr], nums[i]
                curr += 1