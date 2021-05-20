class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        
        nums = sorted(nums)
        res, streak = 0, 0
        print(nums)
        
        for i in range(len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                streak += 1
            elif nums[i] == nums[i+1]:
                pass
            else:
                res = max(res, streak)
                streak = 0
        return max(res, streak) + 1