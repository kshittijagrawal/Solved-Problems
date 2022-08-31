class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        cand = nums[0]
        for i in range(1, len(nums)):
            if abs(nums[i]) < abs(cand): cand = nums[i]
            elif abs(nums[i]) == abs(cand): cand = nums[i] if nums[i] > cand else cand
        return cand
        