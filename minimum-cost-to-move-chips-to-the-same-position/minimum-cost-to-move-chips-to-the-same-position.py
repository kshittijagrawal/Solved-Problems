class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        o, e = 0, 0
        for i in range(len(position)):
            if position[i] % 2 == 0:
                e += 1
            else:
                o += 1
        return min(o, e)