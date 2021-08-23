class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        container = [(v, l) for v, l in sorted(zip(values, labels), reverse=True)]
        labelused, res = {}, 0
        for v, l in container:
            labelused[l] = labelused.get(l, 0) + 1
            if labelused[l] > useLimit: continue
                
            res += v
            
            numWanted -= 1
            if numWanted == 0:
                break
        return res