class Solution:
    def decodeString(self, s: str) -> str:
        stack = collections.deque()
        
        for i in range(len(s)):
            if s[i] == "]":
                seq = collections.deque()
                while stack and stack[-1] != "[":
                    seq.appendleft(stack.pop())
                
                stack.pop()
                num = collections.deque()
                while stack and stack[-1].isdigit():
                    num.appendleft(stack.pop())
                
                stack.append(int("".join(num)) * "".join(seq))
            else:
                stack.append(s[i])
        
        return "".join(stack)