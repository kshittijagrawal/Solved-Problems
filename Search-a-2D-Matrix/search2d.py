class Solution:
    def searchMatrix(self, matrix, target):
        for i in matrix:
            if i[-1] < target:
                continue
            lo, hi = 0, len(i)-1
            while lo<= hi:
                mid = lo + ((hi-lo)//2)
                if i[mid] == target:
                    return True
                elif i[mid] > target:
                    hi = mid-1
                else:
                    lo = mid+1
            return False
        return False