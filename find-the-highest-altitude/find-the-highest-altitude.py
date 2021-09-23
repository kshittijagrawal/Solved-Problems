class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curmax, curh = 0, 0
        for i in range(len(gain)):
            curh += gain[i]
            curmax = max(curmax, curh)
        
        return curmax