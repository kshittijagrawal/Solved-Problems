class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        res = prev = currsum = 0
        
        for i in range(len(nums)):
            
            if i >= k:
                if len(d) == k:
                    res = max(res, currsum)
                currsum -= nums[prev]
                d[nums[prev]] -= 1
                if not d[nums[prev]]:
                    del d[nums[prev]]
                prev += 1

                
            currsum += nums[i]
            d[nums[i]] = d.get(nums[i], 0) + 1
        
        if currsum > res and len(d) == k:
            return currsum
        return res
