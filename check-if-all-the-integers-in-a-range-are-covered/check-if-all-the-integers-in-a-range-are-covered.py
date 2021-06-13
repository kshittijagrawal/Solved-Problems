class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for current in range(left, right+1):
            i = 0
            while i<len(ranges):
                if ranges[i][0] <= current <= ranges[i][1]:
                    break
                i += 1
            else:
                return False
        
        return True