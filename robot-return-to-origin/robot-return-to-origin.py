class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = collections.Counter(moves)
        return False if c["L"] != c["R"] or c["U"] != c["D"] else True