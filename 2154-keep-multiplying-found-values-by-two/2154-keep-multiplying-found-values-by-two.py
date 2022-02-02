class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        container = collections.Counter(nums)
        while container.get(original, 0):
            original *= 2
        return original