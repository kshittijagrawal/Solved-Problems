class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res, curr = 0, 0
        for i, t in enumerate(timeSeries):
            if i > 0 and curr >= t:
                res = res - (curr - t + 1)
            res += duration
            curr = t + duration - 1
        return res