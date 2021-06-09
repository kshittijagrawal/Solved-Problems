class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        row, col = 0, 0
        board = {}
        for i in "abcdefghijklmnopqrstuvwxyz":
            board[i] = (row, col)
            col += 1
            if col == 5:
                row, col = row+1, 0

        curR, curC, res = 0, 0, ""
        for i in target:
            r, c = board[i]
            if c<curC : res += (curC-c)*"L"
            if r<curR : res += (curR-r)*"U"
            if c>curC : res += (c-curC)*"R"
            if r>curR : res += (r-curR)*"D"
            res += "!"
            curR, curC = r, c
        return res