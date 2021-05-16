class Solution:
    def getRow(self, rowIndex):
        if rowIndex < 2:
            return [1] if rowIndex == 0 else [1,1]
        prev = [1,1]
        for i in range(2, rowIndex+1):
            row = [0]*(i+1)
            row[0], row[-1] = 1, 1
            for j in range(1, i):
                row[j] = prev[j]+prev[j-1]
            prev = row.copy()
        return row