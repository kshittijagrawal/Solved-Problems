class Solution:
    def isPathCrossing(self, path: str) -> bool:
        s, curr = {(0, 0)}, (0, 0)
        
        for c in path:
            if c == "N":
                curr = (curr[0], curr[1] + 1)
            elif c == "S":
                curr = (curr[0], curr[1] - 1)
            elif c == "E":
                curr = (curr[0] + 1, curr[1])
            else:
                curr = (curr[0] - 1, curr[1])
            
            if curr in s:
                return True
            s.add(curr)
        
        return False