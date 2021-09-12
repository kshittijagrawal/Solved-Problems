class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row, col = [0] * m, [0] * n
        
        for r, c in indices:
            row[r], col[c] = row[r] + 1, col[c] + 1
        
        rcount, ccount = {'e':0, 'o':0}, {'e':0, 'o':0}
        for r in row:
            if r%2 == 0: rcount['e'] += 1
            else: rcount['o'] += 1
        
        for c in col:
            if c%2 == 0: ccount['e'] += 1
            else: ccount['o'] += 1
        
        return rcount['e']*ccount['o'] + rcount['o']*ccount['e']