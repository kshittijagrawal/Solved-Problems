class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def finalword(string):
            stack = []
            for char in string:
                if char != "#":
                    stack.append(char)
                else:
                    if not stack: continue
                    stack.pop()
            return "".join(stack)
        
        return finalword(s) == finalword(t)