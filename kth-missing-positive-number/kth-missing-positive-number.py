class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        expected, gap = 1, 0
        
        for i in range(len(nums)):
            gap += nums[i] - expected
            
            if gap >= k:
                return nums[i] - (gap - k) - 1
            
            expected = nums[i] + 1
        
        return nums[-1] + k - gap