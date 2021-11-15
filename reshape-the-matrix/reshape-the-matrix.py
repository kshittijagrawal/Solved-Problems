class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c: return mat
        res = [[0 for _ in range(c)] for _ in range(r)]
        mind, nind = 0, 0
        for i in range(r):
            for j in range(c):
                res[i][j] = mat[mind][nind]
                nind += 1
                if nind == n:
                    mind += 1
                    nind = 0
        return res