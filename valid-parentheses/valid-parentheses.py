class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque()
        close = {")": "(", "]": "[", "}": "{"}
        
        for i in range(len(s)):
            if s[i] not in close:
                stack.append(s[i])
            else:
                if stack and close[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return False if stack else True