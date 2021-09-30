class Solution:
    def sumZero(self, n: int) -> List[int]:
        res, curr = [], 1
        for _ in range(n//2):
            res.append(curr)
            res.append(-curr)
            curr += 1
        
        if n % 2: res.append(0)
        return res