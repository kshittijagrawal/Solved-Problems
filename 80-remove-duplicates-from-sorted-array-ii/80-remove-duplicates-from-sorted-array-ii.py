class Solution:
    def removeDuplicates(self, nums):
        currcount, i = 1, 1
        for ind in range(1, len(nums)):
            if nums[ind] == nums[ind-1]:
                currcount += 1
            if (nums[ind] == nums[ind-1] and currcount<=2):
                nums[i] = nums[ind]
                i += 1
                continue
            if nums[ind] != nums[ind-1]:
                nums[i] = nums[ind]
                currcount = 1
                i += 1
        return i