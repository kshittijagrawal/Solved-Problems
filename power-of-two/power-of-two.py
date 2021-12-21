class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        return (math.log10(n)/math.log10(2)) % 1 == 0