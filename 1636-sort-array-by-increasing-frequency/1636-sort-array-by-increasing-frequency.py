class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        return sorted(nums, key = lambda x: (c[x], -x))