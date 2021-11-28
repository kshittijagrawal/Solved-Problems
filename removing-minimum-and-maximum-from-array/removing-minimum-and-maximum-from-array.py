class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minn, maxx, n = [float("inf"), -1], [float("-inf"), -1], len(nums)
        for i in range(n):
            if nums[i] > maxx[0]: maxx = [nums[i], i]
            if nums[i] < minn[0]: minn = [nums[i], i]
        
        if minn[1] > maxx[1]: minn, maxx = maxx, minn
        return min(maxx[1] + 1, n - minn[1], minn[1] + 1 + n - maxx[1])
        