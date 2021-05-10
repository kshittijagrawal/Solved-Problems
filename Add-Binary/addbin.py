class Solution:
    def addBinary(self, a, b):
        
        if len(a) >= len(b): a,b = a, "0"*(len(a)-len(b)) + b
        else: a,b = "0"*(len(b)-len(a)) + a, b
        
        carry, res = 0, ""
        for i in range(len(a)-1, -1, -1):
            if (a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0"):
                if carry == 0:
                    res = "1"+res
                    carry = 0
                else:
                    res = "0"+res
                    carry = 1
            
            else:
                res = "0"+res if carry == 0 else "1"+res
                if a[i] == "1": carry = 1
                else: carry = 0

        if carry == 1: return "1"+res
        return res