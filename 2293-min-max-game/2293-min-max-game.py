class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            ismin, n = 1, n // 2
            for i in range(n):
                nums[i] = min(nums[i*2], nums[i*2 + 1]) if ismin else max(nums[i*2], nums[i*2 + 1])
                ismin = not ismin
        return nums[0]