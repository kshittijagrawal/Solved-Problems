class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = sum(nums)
        presum = 0
        for i, num in enumerate(nums):
            if presum == totalsum-num:
                return i
            presum += num
            totalsum -= num
        return -1