class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n // 2):
            n -= 1
            for j in range(len(matrix)):
                matrix[j][i], matrix[j][n] = matrix[j][n], matrix[j][i]