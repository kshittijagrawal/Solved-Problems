class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ind = 0
        for i, el in enumerate(nums):
            if el%2 != 0:
                ind = i
                break
                
        for i in range(ind+1, len(nums)):
            if nums[i]%2 == 0:
                nums[i], nums[ind] = nums[ind], nums[i]
                ind += 1
        return nums