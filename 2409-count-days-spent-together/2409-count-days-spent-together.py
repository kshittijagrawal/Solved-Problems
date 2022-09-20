class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        aa = tuple(map(int, arriveAlice.split("-")))
        la = tuple(map(int, leaveAlice.split("-")))
        ab = tuple(map(int, arriveBob.split("-")))
        lb = tuple(map(int, leaveBob.split("-")))
        
        lower, upper = max(aa, ab), min(la, lb)

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        lower_sum, upper_sum = 0, 0
        for i in range(lower[0] - 1):
            lower_sum += days[i]
        for i in range(upper[0] - 1):
            upper_sum += days[i]
        
        res = (upper_sum + upper[1]) - (lower_sum + lower[1]) + 1
        return res if res > 0 else 0