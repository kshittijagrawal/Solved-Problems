class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons, self.times = persons, times
        c, self.leading = {}, []
        maxcount = maxcan = None
        for i, p in enumerate(self.persons):
            c[p] = c.get(p, 0) + 1
            if not maxcount or c[p] >= maxcount:
                self.leading.append(p)
                maxcount, maxcan = c[p], p
            else:
                self.leading.append(maxcan)
        print(self.leading)
        

    def q(self, t: int) -> int:
        lo, hi = 0, len(self.times) - 1
        mid = 0
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if self.times[mid] == t:
                break
            elif self.times[mid] > t:
                hi = mid - 1
            else:
                lo = mid + 1
        else: mid = lo - 1
        return self.leading[mid]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)