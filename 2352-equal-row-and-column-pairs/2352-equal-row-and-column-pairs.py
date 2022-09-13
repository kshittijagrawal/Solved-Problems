class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        container = {}
        for row in grid:
            container[tuple(row)] = container.get(tuple(row), 0) + 1
        
        res = 0
        for r in range(len(grid)):
            column = []
            for c in range(len(grid[0])):
                column.append(grid[c][r])
            res += container.get(tuple(column), 0)
        return res