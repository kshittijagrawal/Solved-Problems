class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        container = {}
        for i in range(len(nums)):
            container[nums[i]] = container.get(nums[i], 0) + 1
            if container[nums[i]] > 1:
                return True
        return False