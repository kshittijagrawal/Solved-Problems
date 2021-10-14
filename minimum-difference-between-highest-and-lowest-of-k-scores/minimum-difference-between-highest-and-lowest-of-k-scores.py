class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i, res = 0, float("inf")
        for j in range(k-1, len(nums)):
            res = min(res, nums[j] - nums[i])
            i += 1
            
        return res