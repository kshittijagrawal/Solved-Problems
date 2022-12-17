class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        
        stack = collections.deque()
        for i in tokens:
            if i == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(first) - int(second))
            elif i == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif i == "/":
                second = stack.pop()
                first = stack.pop()
                stack.append(int(int(first) / int(second)))
            else:
                stack.append(i)
        return stack[0]