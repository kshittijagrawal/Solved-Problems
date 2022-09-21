class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res, currsum = [], 0
        
        for num in nums:
            if num % 2 == 0:
                currsum += num
                
        for val, ind in queries:
            if nums[ind] % 2 == 0:
                currsum -= nums[ind]
            
            nums[ind] += val
            
            if nums[ind] % 2 == 0:
                currsum += nums[ind]
            
            res.append(currsum)
        
        return res