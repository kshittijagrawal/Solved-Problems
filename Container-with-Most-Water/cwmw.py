class Solution:
    def maxArea(self, h):
        area, maxi = 0, 0
        i, j = 0, len(h)-1
        while(i<=j):
            if h[i] >= h[j]:
                area = (j-i) * h[j]
                j -= 1
            else:
                area = (j-i) * h[i]
                i += 1
            if area >= maxi: maxi = area
        return maxi