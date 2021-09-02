import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if math.sqrt(c) % 1 == 0: # if number is a perfect square
            return True
        
        for a in range(int(math.sqrt(c)) + 1):
            b = math.sqrt(c - a**2)
            if b % 1 == 0:
                return True
        return False