class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, first in enumerate(nums):
            second = target - first
            if second not in d:
                d[first] = i
            else:
                return [d[second], i]