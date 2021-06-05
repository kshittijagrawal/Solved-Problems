class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        newp = list(palindrome)
        for i in range(len(newp)//2):
            if newp[i] != "a":
                newp[i] = "a"
                return "".join(newp)
        
        newp[-1] = "b"
        return "".join(newp)