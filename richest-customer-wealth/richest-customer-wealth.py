class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for person in accounts:
            res = max(res, sum(person))
        
        return res