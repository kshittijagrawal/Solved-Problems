class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            return self.myPow(1/x, -n)
        elif n%2 == 0:
            res = self.myPow(x, n//2)
            return res * res
        else:
            return x*self.myPow(x, n-1)
        