class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        presum, res = 0, -1
        for i, num in enumerate(nums):
            if (total - num) / 2 == presum:
                res = i
                break
            presum += num
        return res