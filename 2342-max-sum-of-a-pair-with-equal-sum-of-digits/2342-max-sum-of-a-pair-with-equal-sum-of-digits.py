class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        def digitsum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        c = collections.defaultdict(list)
        for num in nums:
            s = digitsum(num)
            if len(c[s]) == 2:
                if num > c[s][-1]:
                    c[s].pop()
                    c[s].append(num)
            else:
                c[s].append(num)
            
            if len(c[s]) == 2:
                if c[s][-1] > c[s][0]:
                    c[s][-1], c[s][0] = c[s][0], c[s][-1]
        
        res = -1
        for key in c:
            if len(c[key]) == 2:
                res = max(res, sum(c[key]))
        
        return res