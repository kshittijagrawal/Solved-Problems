class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        front, rear = 0, len(nums) - 1
        while front < rear:
            if nums[front] % 2 != 0 and nums[rear] % 2 == 0:
                nums[front], nums[rear] = nums[rear], nums[front]
                rear -= 1
                front += 1
            elif nums[front] % 2 == 0 and nums[rear] % 2 != 0:
                front += 1
                rear -= 1
            elif nums[front] % 2 != 0 and nums[rear] % 2 != 0:
                rear -= 1
            else:
                front += 1
        
        return nums