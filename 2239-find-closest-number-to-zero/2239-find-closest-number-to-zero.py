class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        diff, cand = float("inf"), float("inf")
        for num in nums:
            if abs(num) < diff:
                diff = abs(num)
                cand = num
            elif abs(num) == diff:
                cand = num if num > cand else cand
        return cand
        