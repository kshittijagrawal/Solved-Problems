class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 0
        for i in range(1, min(a, b) + 1):
            res += a%i == 0 and b%i == 0
        return res