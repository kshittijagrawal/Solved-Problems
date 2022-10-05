class Solution:
    def maxSum(self, x: List[List[int]]) -> int:
        res = 0
        
        for i in range(len(x) - 2):
            for j in range(len(x[0]) - 2):

                m = 0
                for k in range(j, j+3):
                    m += x[i][k]
                
                for k in range(j, j+3):
                    m += x[i+2][k]
                
                m += x[i+1][j+1]
                if m > res: res = m
        return res