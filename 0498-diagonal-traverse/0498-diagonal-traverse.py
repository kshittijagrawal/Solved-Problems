class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res, m, n = [], len(mat), len(mat[0])
        i = j = 0
        updown = 1
        
        for _ in range(m * n):
            res.append(mat[i][j])
            
            if updown:
                i, j = i - 1, j + 1
                if j >= n:
                    i, j = i + 2, j - 1
                    updown = not updown
                elif i < 0:
                    i = 0
                    updown = not updown
                    
            else:
                i, j = i + 1, j - 1
                if i >= m:
                    i, j = i - 1, j + 2
                    updown = not updown
                elif j < 0:
                    j = 0
                    updown = not updown
            
        return res