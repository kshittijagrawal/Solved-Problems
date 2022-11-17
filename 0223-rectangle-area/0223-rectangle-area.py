class Solution:
    def computeArea(self, a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int) -> int:

        total = (c - a) * (d - b) + (g - e) * (h - f)
        
        width = max(0, min(c, g) - max(a, e))
        height = max(0, min(d, h) - max(b, f))
        
        return total - width * height