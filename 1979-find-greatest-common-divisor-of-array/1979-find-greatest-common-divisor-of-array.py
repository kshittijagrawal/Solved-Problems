class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b%a, a)
        
        min = max = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min:
                min = nums[i]
            if nums[i] > max:
                max = nums[i]
        return gcd(min, max)
        