class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = []
        c = {}
        for num in nums:
            for n in num:
                c[n] = c.get(n, 0) + 1
        
        l = len(nums)
        for i in range(1, 1001):
            if c.get(i, 0) == l:
                res.append(i)
        
        return res