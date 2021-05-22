class Solution:
    def generateMatrix(self, n: int):
        res = [[0 for i in range(n)] for j in range(n)]
        
        r = c = 0
        lr = lb = len(res)
        ll, lt = -1, 0
        
        iterations = curr = 1
        while iterations <= len(res)//2:
            
            while c<lr:
                res[r][c] = curr
                curr += 1
                c += 1
            c, r, lr = c-1, r+1, lr-1
            
            while r<lb:
                res[r][c] = curr
                curr += 1
                r += 1
            c, r, lb = c-1, r-1, lb-1
            
            while c>ll:
                res[r][c] = curr
                curr += 1
                c -= 1
            c, r, ll = c+1, r-1, ll+1
            
            while r>lt:
                res[r][c] = curr
                curr += 1
                r -= 1
            c, r, lt = c+1, r+1, lt+1
            iterations += 1
    
        if n%2 != 0: res[r][c] = curr
        return res