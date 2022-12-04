class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        n, totalSum, leftSum = len(nums), sum(nums), 0
        res = [inf, inf]
        
        for i, v in enumerate(nums):
            leftSum += v
            
            leftAvg = leftSum // (i + 1)
            rightAvg = (totalSum - leftSum) // (n - i - 1) if n - i - 1 != 0 else 0
            absDif = abs(leftAvg - rightAvg)
            
            res = min(res, [absDif, i])
        
        return res[1]