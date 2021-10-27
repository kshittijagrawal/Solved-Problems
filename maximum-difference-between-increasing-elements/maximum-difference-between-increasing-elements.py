class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        currmin, res = nums[0], None
        for i in range(1, len(nums)):
            if nums[i] < currmin:
                currmin = nums[i]
                continue
            res = max(res, nums[i] - currmin) if res else nums[i] - currmin
        
        return res if res else -1