class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        c = {heights[i]: i for i in range(len(heights))}
        heights.sort()
        res = []
        for i in range(len(heights)-1, -1, -1):
            res.append(names[c[heights[i]]])
        return res
        