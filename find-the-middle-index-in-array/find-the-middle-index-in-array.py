class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prev, tsum = 0, sum(nums)
        for i in range(len(nums)):
            if tsum - nums[i] == prev:
                return i
            prev, tsum = prev + nums[i], tsum - nums[i]
        return -1