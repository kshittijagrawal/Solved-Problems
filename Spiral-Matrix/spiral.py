class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c, res = 0, 0, []
        lr , lb = len(matrix[0]), len(matrix)
        ll, lt = -1, 0
        executed = 0
        
        iterations = 1
        while iterations <= (len(matrix)//2)+1:
            
            while c<lr:
                res.append(matrix[r][c])
                c += 1
                executed = 1
            if executed == 0: break
            executed = 0
            lr -= 1
            c, r = c-1, r+1
            
            while r<lb:
                res.append(matrix[r][c])
                r += 1
                executed = 1
            if executed == 0: break
            executed = 0
            lb -= 1
            c, r = c-1, r-1
            
            while c>ll:
                res.append(matrix[r][c])
                c -= 1
                executed = 1
            if executed == 0: break
            executed = 0
            ll += 1
            c, r = c+1, r-1
            
            while r>lt:
                res.append(matrix[r][c])
                r -= 1
                executed = 1
            if executed == 0: break
            executed = 0
            lt += 1
            c, r = c+1, r+1
            iterations += 1
            
        return res