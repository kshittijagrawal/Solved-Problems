class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        container = collections.Counter(nums)
        return sorted(nums, key = lambda x: (container[x], -x))