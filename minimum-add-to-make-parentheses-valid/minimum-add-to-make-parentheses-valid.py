class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = collections.deque()
        for i in s:
            if i == "(":
                stack.append(i)
            else:
                if len(stack) == 0:
                    stack.append(i)
                elif stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(i)        
        return len(stack)