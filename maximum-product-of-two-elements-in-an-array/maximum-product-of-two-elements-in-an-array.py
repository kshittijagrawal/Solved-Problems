class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxnum, maxind = float("-inf"), 0
        for ind, num in enumerate(nums):
            if num > maxnum:
                maxnum, maxind = num, ind
        
        secondmax = float("-inf")
        for ind, num in enumerate(nums):
            if num > secondmax and ind != maxind:
                secondmax = num
        
        return (maxnum-1)*(secondmax-1)