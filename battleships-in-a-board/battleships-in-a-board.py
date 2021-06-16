class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res, row, col = 0, len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == "X":
                    if (j == col-1) and (i < row-1):
                        if (board[i+1][j] == "."):
                            res += 1
                        else:
                            continue
                    elif (i == row-1) and (j < col-1):
                        if (board[i][j+1] == "."):
                            res += 1
                        else:
                            continue
                    elif (i == row-1) and (j == col-1):
                        res += 1
                    elif (board[i+1][j] == ".") and (board[i][j+1] == "."):
                        res += 1
        return res
                        