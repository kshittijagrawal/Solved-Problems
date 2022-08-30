class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        extra = 1 if 0 in s else 0
        return len(s) - extra
            