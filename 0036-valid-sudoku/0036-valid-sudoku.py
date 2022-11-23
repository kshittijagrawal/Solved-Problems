class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = set()
        c = set()
        b = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                if (i, board[i][j]) in r or (j, board[i][j]) in c or (i//3, j//3, board[i][j]) in b:
                    return False
                r.add((i, board[i][j]))
                c.add((j, board[i][j]))
                b.add((i//3, j//3, board[i][j]))
        return True