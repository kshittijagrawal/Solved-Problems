class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        stack, res = collections.deque(), [-1]*length
        for i in range(length*2):
            while stack and stack[-1][0] < nums[i%length]:
                ele, ind = stack.pop()
                res[ind] = nums[i%length]
            stack.append((nums[i%length], i%length))
        return res