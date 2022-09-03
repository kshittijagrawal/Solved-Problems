class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            arr = [0] * (len(nums) - 1)
            for i in range(1, len(nums)):
                arr[i-1] = (nums[i-1] + nums[i]) % 10
            nums = arr
            
        return nums[0]