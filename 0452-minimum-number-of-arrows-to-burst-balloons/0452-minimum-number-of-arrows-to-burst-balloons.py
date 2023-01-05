class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        echeck = points[0][1]
        res = 1
        
        for i in range(1, len(points)):
            start, end = points[i]
            if start <= echeck:
                continue
            res += 1
            echeck = end
        
        return res