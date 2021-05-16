class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1], [1,1]]
        if numRows <= 2:
            return [[1]] if numRows == 1 else ans
        for i in range(3, numRows+1):
            row = [0]*i
            row[0], row[-1] = 1, 1
            for j in range(1, i-1):
                row[j] = ans[-1][j] + ans[-1][j-1]
            ans.append(row)
        return ans