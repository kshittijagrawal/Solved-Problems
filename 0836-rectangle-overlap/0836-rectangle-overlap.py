class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        a, b, c, d = rec1
        e, f, g, h = rec2
        
        width = max(0, min(c, g) - max(a, e))
        height = max(0, min(d, h) - max(b, f))
        
        return True if width * height > 0 else False