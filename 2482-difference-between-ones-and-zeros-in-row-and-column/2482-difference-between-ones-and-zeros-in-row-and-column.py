class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ones_row = [0] * m
        ones_col = [0] * n
        
        for i in range(m):
            ones_row_count = 0
            for j in range(n):
                if grid[i][j] == 1:
                    ones_row_count += 1
                    ones_col[j] += 1
            
            ones_row[i] += ones_row_count
        
        for i in range(m):
            for j in range(n):
                grid[i][j] = ones_row[i] + ones_col[j] - (m - ones_row[i]) - (n - ones_col[j])
        
        return grid