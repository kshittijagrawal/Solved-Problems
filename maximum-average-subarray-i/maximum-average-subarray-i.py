class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res, preindex, cursum = None, 0, 0
        for i in range(len(nums)):
            cursum += nums[i]
            if i >= k - 1:
                res = max(res, cursum) if res else cursum
                cursum -= nums[preindex]
                preindex += 1
        
        return res/k