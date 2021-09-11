class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        cr, cc, res = 0, nc - 1, 0
        
        while cr < nr and cc >= 0:
            if grid[cr][cc] < 0:
                res += nr - cr
                cc -= 1
                
            else:
                cr += 1
        
        return res