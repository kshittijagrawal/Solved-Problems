class Solution:
    def removeElement(self, nums, val):
        i = 0
        for el in nums:
            if el != val:
                nums[i] = el
                i += 1
        return i