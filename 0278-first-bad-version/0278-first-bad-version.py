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
            m = lo + (hi - lo) // 2
            outcome = isBadVersion(m)
            
            if outcome:
                hi = m
            else:
                lo = m + 1
                
        return lo