class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum = count = 0
        for num in nums:
            if num % 6 == 0:
                sum, count = sum + num, count + 1
        return sum // count if count else count