class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.append(0)
        n, twice, missing = len(nums), 0, 0
        for i in range(n):
            nums[nums[i] % n] += n
        
        for i in range(n):
            if nums[i]//n == 2: twice = i
            if nums[i]//n == 0: missing = i
        
        return [twice, missing]