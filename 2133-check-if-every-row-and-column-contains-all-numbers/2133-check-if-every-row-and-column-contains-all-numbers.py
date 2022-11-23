class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        r = set()
        c = set()
        n = len(matrix)
        
        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                if not 1 <= num <= n or (i, num) in r or (j, num) in c:
                    return False
                r.add((i, num))
                c.add((j, num))
        return True