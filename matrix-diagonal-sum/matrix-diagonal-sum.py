class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        col = length - 1
        res = 0
        for i in range(length):
            c1, c2 = i, col
            res += mat[i][c1] + mat[i][c2]
            col -= 1
        
        return res - mat[length//2][length//2] if length%2 != 0 else res