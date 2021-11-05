class Solution:
    def arrangeCoins(self, n: int) -> int:
        res, i = 0, 1
        while n > 0:
            res += 1
            n, i = n - i, i + 1
        return res - 1 if n < 0 else res