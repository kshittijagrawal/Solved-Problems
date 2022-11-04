class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        def calc_sum(num):
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s
        
        res , itr = 0, 1
        while calc_sum(n) > target:
            newn = (n // (10 ** itr) + 1) * (10 ** itr)
            res += (newn - n)
            n = newn
            itr += 1
        return res