class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if (len(nums) == 1) and (k % 2 != 0):
            return -1
        
        currmax, i, K = -1, 0, k
        while i < len(nums) and k > 1:
            currmax = max(currmax, nums[i])
            i += 1
            k -= 1
        
        if len(nums) > K:
            currmax = max(currmax, nums[K])
        return currmax