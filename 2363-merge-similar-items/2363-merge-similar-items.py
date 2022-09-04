class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        c = {v : w for v, w in items1}
        for v, w in items2:
            c[v] = c.get(v, 0) + w
        return [[v, w] for v, w in sorted(c.items())]
            