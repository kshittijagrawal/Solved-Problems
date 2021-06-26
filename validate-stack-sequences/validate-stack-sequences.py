class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, j = [], 0
        for num in pushed:
            stack.append(num)
            
            while len(stack) != 0 and j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
        return True if j == len(popped) else False