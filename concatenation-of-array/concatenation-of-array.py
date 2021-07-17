class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n*2
        for i in range(n):
            res[i] = res[i+n] = nums[i]
        return res