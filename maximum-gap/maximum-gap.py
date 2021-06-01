class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        _max = -float("inf")
        
        for i in range(1, len(nums)):
            curr = nums[i] - nums[i-1]
            _max = max(_max, curr)
        return _max if _max!=-float("inf") else 0
# Time - Linearithmic
# Space - Constant
    

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        mi, ma, n = min(nums), max(nums), len(nums)
        if mi == ma: return 0  # All elements are the same
        bucketSize = math.ceil((ma - mi) / (n - 1))
        minBucket = [math.inf] * n
        maxBucket = [-math.inf] * n
        
        for x in nums:
            idx = (x - mi) // bucketSize
            minBucket[idx] = min(minBucket[idx], x)
            maxBucket[idx] = max(maxBucket[idx], x)

        maxGap = bucketSize  # Maximum gap is always greater or equal to bucketSize
        prev = maxBucket[0]  # We always have 0th bucket
        
        for i in range(1, n):
            if minBucket[i] == math.inf: continue  # Skip empty bucket
            maxGap = max(maxGap, minBucket[i] - prev)
            prev = maxBucket[i]
        return maxGap  
# Time - Linear
# Space - Linear
