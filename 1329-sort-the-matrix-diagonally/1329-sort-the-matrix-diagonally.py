class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        r, c = len(mat), len(mat[0])
        formula = 2*min(r, c) + (abs(r - c) - 1) #total number of diagonals
        starti, startj = r - 1, 0
        
        for _ in range(formula):
            diag, i, j = [], starti, startj
            
            while i < r and j < c:
                diag.append(mat[i][j])
                i, j = i + 1, j + 1
                
            diag.sort()
            i, j = i - 1, j - 1
            
            while i >= 0 and j >= 0:
                mat[i][j] = diag.pop()
                i, j = i - 1, j - 1
            
            if starti == 0: startj += 1
            else: starti -= 1
        
        return mat