class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            for i in range(1, n):
                nums[i-1] = (nums[i-1] + nums[i]) % 10
            n -= 1
        return nums[0]