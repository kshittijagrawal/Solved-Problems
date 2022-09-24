class Solution:
    def countElements(self, nums: List[int]) -> int:
        gmin = float("inf")
        gmax = float("-inf")
        c = {}
        for num in nums:
            gmax = max(gmax, num)
            gmin = min(gmin, num)
            c[num] = c.get(num, 0) + 1
        
        res = len(nums) - c[gmin] - c[gmax]
        return res if res > 0 else 0