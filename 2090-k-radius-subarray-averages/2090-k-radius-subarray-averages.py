class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n
        presum = preindex = 0
        index = k
        
        for i, num in enumerate(nums):
            presum += num
            if i >= 2*k:
                res[index] = presum // (2*k + 1)
                presum -= nums[preindex]
                preindex, index = preindex + 1, index + 1
        return res
                
        