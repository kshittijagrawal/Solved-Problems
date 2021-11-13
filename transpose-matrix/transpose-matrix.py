class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        res = [[matrix[j][i] for j in range(r)]for i in range(c)]
        return res