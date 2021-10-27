class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        container, res = {}, 0
        for i in range(len(nums)):
            container[nums[i]] = container.get(nums[i], 0) + 1
            res += container.get(nums[i]+k, 0) + container.get(nums[i]-k, 0)
        return res