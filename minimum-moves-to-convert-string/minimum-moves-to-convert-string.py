class Solution:
    def minimumMoves(self, s: str) -> int:
        index, res = 0, 0
        while index < len(s):
            if s[index] == "X":
                res += 1
                index += 3
            else:
                index += 1
        
        return res