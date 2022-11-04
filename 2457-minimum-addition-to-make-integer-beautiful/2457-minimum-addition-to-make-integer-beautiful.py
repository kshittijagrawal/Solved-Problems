class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        def calc_sum(num):
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s
        
        res , itr = 0, 10
        while calc_sum(n) > target:
            newn = (n // itr + 1) * itr
            res += (newn - n)
            n = newn
            itr *= 10
        return res