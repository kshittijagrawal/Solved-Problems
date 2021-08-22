class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        freqs = [0]*101
        for height in heights:
            freqs[height] += 1
        
        hindex, findex = 0, 0
        res = 0
        while findex < 101 and hindex < len(heights):
            if freqs[findex] == 0:
                findex += 1
                continue
            
            if heights[hindex] == findex:
                freqs[findex] -= 1
                hindex += 1
            else:
                res += 1
                freqs[findex] -= 1
                hindex += 1
                
        return res