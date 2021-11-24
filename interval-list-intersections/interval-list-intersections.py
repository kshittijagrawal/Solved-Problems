class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            f, s = max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])
            if f <= s: res.append([f, s])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res