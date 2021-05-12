class Solution:
    def mySqrt(self, x):
        lo, hi = 0, x
        while lo <= hi:
            mid = lo + ((hi-lo)//2)
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                hi = mid-1
            else:
                lo = mid+1
        return hi