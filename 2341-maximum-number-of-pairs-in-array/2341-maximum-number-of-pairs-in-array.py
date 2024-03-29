class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = lefts = 0
        c = {}
        for num in nums:
            if c.get(num):
                pairs, lefts = pairs + 1, lefts - 1
                c[num] -= 1
            else:
                lefts += 1
                c[num] = 1
        return [pairs, lefts]