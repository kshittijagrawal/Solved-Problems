class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 2:
            return [[1]] if numRows == 1 else [[1], [1,1]]
        res = [[1], [1,1]]
        for i in range(2, numRows):
            a = [1] * (i + 1)
            for j in range(1, i):
                 a[j] = res[-1][j] + res[-1][j - 1]
            res.append(a)
        return res