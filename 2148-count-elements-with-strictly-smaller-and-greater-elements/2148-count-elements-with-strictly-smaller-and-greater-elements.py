class Solution:
    def countElements(self, nums: List[int]) -> int:
        gmin = float("inf")
        gmax = float("-inf")
        for num in nums:
            gmax = max(gmax, num)
            gmin = min(gmin, num)
        
        res = 0
        for num in nums:
            if num != gmax and num != gmin:
                res += 1
        
        return res