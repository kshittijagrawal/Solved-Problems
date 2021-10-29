class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max2 = float("-inf")
        min1 = min2 = float("inf")
        
        for i in range(len(nums)):
            
            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] <= min2:
                min2 = nums[i]
            
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
            elif nums[i] >= max2:
                max2 = nums[i]
                
        return max1*max2 - min1*min2