class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = str(num)
        res = nums
        for i in range(len(nums)):
            if nums[i] == "6":
                res = nums[:i] + "9" + nums[i+1:]
                break
        return res