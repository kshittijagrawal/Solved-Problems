class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        res = 0
        for a, b in zip(seats, students):
            res += abs(a - b)
        
        return res