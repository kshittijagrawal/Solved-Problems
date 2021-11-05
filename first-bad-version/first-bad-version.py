# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            call = isBadVersion(mid)
            if call:
                hi = mid
            else:
                lo = mid + 1
        return hi