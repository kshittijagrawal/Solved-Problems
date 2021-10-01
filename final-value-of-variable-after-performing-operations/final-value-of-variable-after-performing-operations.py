class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for c in operations:
            if c[1] == '+':
                res += 1
            else:
                res -= 1
        
        return res