class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n, onein1, onein2 = len(img1), [], []
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    onein1.append((i, j))
                if img2[i][j] == 1:
                    onein2.append((i, j))
        
        container, res = {}, 0
        for x1, y1 in onein1:
            for x2, y2 in onein2:
                diff = x2 - x1, y2 - y1
                container[diff] = container.get(diff, 0) + 1
                res = max(res, container[diff])
        return res
                