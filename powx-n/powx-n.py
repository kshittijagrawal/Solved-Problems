class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        if not n % 2:
            prod = self.myPow(x, n // 2)
            return prod*prod
        else:
            prod = self.myPow(x, (n-1) // 2)
            return prod * prod *x