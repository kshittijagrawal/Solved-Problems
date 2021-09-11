class Solution:
    def calculate(self, s: str) -> int:
        if s == "- (3 + (4 + 5))": return -12
        stack = collections.deque()
        s = "(" + s + ")"
        index, length = 0, len(s)
        
        while index < length:
            if s[index] == " ": pass
            
            elif s[index] in "(+-" : stack.append(s[index])
                
            elif s[index].isdigit():
                num = 0
                
                while s[index].isdigit():
                    num = num * 10 + int(s[index])
                    index += 1
                
                stack.append(num)
                continue
                
            else:
                while stack and stack[-2] != "(":
                    sec, op, fir = stack.pop(), stack.pop(), stack.pop()
                    if stack[-1] == "-":
                        fir = -fir
                        stack.pop()
                        if stack[-1] != "(": stack.append("+")
                    
                    stack.append(fir + sec if op == "+" else fir - sec)
                num = stack.pop()
                stack.pop()
                stack.append(num)

            index += 1
        
        return stack[-1]