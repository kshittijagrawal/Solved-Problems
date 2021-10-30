class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ind, l = 0, len(original)
        if l != m*n: return []
        res = [[0 for _ in range(n)]for i in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = original[ind]
                ind += 1
        return res
    