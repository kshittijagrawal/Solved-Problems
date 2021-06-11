class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, x2, x3 = points[0][0], points[1][0], points[2][0]
        y1, y2, y3 = points[0][1], points[1][1], points[2][1]
        
        if abs((x1*(y2-y3)) + (x2*(y3-y1)) + (x3*(y1-y2)))/2 == 0:
            return False
        return True