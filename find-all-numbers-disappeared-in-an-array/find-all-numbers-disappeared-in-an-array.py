class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            a = abs(nums[i]) - 1
            if nums[a] > 0: nums[a] *= -1
                
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
            