class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if not stack or char != stack[-1]:
                stack.append(char)
            else:
                stack.pop()
            
        return "".join(stack)