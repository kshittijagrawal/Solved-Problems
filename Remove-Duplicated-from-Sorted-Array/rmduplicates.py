class Solution:
    def removeDuplicates(self, nums):
        i = 1
        for ind in range(1, len(nums)):
            if nums[ind] != nums[ind-1]:
                nums[i] = nums[ind]
                i += 1
        return i