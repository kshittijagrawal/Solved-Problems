class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        presum, potential = 0, float("inf")
        for i in range(len(nums)):
            presum += nums[i]
            potential = min(potential, presum)
        return 1 if potential > 0 else 1 - potential