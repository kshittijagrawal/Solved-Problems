class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        res, prev = float("inf"), 0
        
        for i, block in enumerate(blocks):
            if block == "W":
                whites += 1
            
            if i + 1 >= k:
                res = min(res, whites)
                whites -= (blocks[prev] == "W")
                prev += 1
        
        return res