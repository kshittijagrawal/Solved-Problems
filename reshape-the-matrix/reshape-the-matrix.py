class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rowlen, collen = len(mat), len(mat[0])
        if r*c != rowlen*collen:
            return mat
        res, row, col = [[0 for i in range(c)] for j in range(r)], 0, 0
        for i in range(r):
            for j in range(c):
                res[i][j] = mat[row][col]
                col += 1
                if col == collen:
                    row, col = row+1, 0
        return res