class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, l1, l2 = 0, len(num1) - 1, len(num2) - 1
        for i in range(l1 + 1):
            n1 += (ord(num1[i]) - 48) * (10**l1)
            l1 -= 1
        
        res = 0
        for i in range(l2 + 1):
            res += n1 * (ord(num2[i]) - 48) * (10**l2)
            l2 -= 1
        
        return str(res)