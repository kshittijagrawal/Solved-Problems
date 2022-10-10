class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        ptime = 0
        maxtime = maxid = 0
        for id, ctime in logs:
            d = ctime - ptime
            if d > maxtime:
                maxtime, maxid = d, id
            elif d == maxtime:
                maxid = maxid if maxid < id else id
            ptime = ctime
        return maxid