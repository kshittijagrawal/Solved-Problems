class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = collections.deque()
        for c in s:
            if c == "(":
                stack.append(c)
            elif c == ")":
                word = ""
                while stack and stack[-1] != "(":
                    word = word + stack.pop()[::-1]
                stack.pop()
                stack.append(word)
            else:
                if not stack or stack[-1] == "(":
                    stack.append(c)
                else:
                    stack[-1] += c
        return "".join(stack)