class Solution:
    def isValidSudoku(self, board):
        
        def row_check():
            for i in range(9):
                row = set()
                for j in range(9):
                    cur = board[i][j]
                    if cur == ".":
                        continue
                    if cur in row:
                        return False
                    row.add(cur)
            return True
        
        def column_check():
            for i in range(9):
                col = set()
                for j in range(9):
                    cur = board[j][i]
                    if cur == ".":
                        continue
                    if cur in col:
                        return False
                    col.add(cur)
            return True
        
        def square_check():
            sqr = set()
            for i in range(9):
                for j in range(9):
                    cur = board[i][j]
                    if cur == ".":
                        continue
                    if (i//3, j//3, cur) in sqr:
                        return False
                    sqr.add((i//3, j//3, cur))
            return True
        
        r = row_check()
        c = column_check()
        s = square_check()
        return True if all((r,c,s)) else False