class Solution:
    def search(self, nums, target):
        flag = 0
        for i in nums:
            if i == target:
                flag = 1
                break
        return flag