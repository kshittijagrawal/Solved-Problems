class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res, flag = [], 0
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
                flag = 1
            elif flag == 1:
                break
        return res