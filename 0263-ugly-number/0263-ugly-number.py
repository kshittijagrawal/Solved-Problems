class Solution:
    def isUgly(self, n: int) -> bool:
        
        if n < 1:
            return False
        
        for pick in [5, 3, 2]:
            while n % pick == 0:
                n //= pick
        
        return n == 1