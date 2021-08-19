class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            lo, hi, mid = 0, n-1, 0
            while lo <= hi:
                mid = lo + ((hi - lo) // 2)
                if grid[i][mid] < 0:
                    if mid == 0 or grid[i][mid - 1] >= 0:break
                
                if grid[i][mid] >= 0:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else: continue
            res += n - mid
        return res