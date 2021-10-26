class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n, res = len(nums), 0
        minarr, maxarr = [None]*n, [None]*n
        minarr[0], maxarr[n-1] = nums[0], nums[n-1]
        
        for i in range(1, n):
            minarr[i] = max(minarr[i-1], nums[i])
            maxarr[n-i-1] = min(maxarr[n-i], nums[n-i-1])
        
        for i in range(1, n-1):
            if minarr[i-1] < nums[i] < maxarr[i+1]:
                res += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                res += 1
        
        return res