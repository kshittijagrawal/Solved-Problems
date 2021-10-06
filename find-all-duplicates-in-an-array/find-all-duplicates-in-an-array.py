class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.append(0)
        n = len(nums)
        res = []
        for i in range(n):
            nums[nums[i] % n] += n
        
        for i in range(n):
            if nums[i] // n == 2:
                res.append(i)
        
        return res