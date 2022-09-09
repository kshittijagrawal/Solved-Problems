class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        res, i = 0, 1
        while i < len(nums)-1:
            prev, nxt = i-1, i+1
            while (nums[nxt] == nums[i]) and (nxt < len(nums)-1): nxt += 1
            if (nums[prev] < nums[i] > nums[nxt]) or (nums[prev] > nums[i] < nums[nxt]):
                res += 1
            i = nxt
        return res