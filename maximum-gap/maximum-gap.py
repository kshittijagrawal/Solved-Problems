class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        _max = -float("inf")
        
        for i in range(1, len(nums)):
            curr = nums[i] - nums[i-1]
            _max = max(_max, curr)
        return _max if _max!=-float("inf") else 0