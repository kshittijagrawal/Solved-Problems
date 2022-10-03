class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        c = {}
        for i in range(1, len(nums)):
            if nums[i-1] == key:
                c[nums[i]] = c.get(nums[i], 0) + 1
        maxc, maxcc = 0, 0
        for k in c:
            if c[k] > maxcc:
                maxc, maxcc = k, c[k]
        return maxc