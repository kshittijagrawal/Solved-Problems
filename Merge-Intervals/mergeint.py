class Solution:
    def merge(self, nums):
        nums = sorted(nums, key = lambda x:x[0])
        res = [nums[0]]
        
        for i in nums[1:]:
            if i[0] <= res[-1][1]:
                res[-1][1] = max(i[1], res[-1][1])
            else:
                res.append(i)
        
        return res