class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        usermap = {}
        for iid, time in logs:
            usermap.setdefault(iid, set()).add(time)
        
        res = [0]*k
        for iid, time in usermap.items():
            res[len(time)-1] += 1
        return res