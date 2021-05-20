class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for i in range(len(s)):
            if s[i].isalnum():
                newstr = newstr + (s[i].lower())
        
        if len(newstr) <= 1:
            return True
                
        front, back = 0, len(newstr)-1
        count = len(newstr)//2 if len(newstr)%2 == 0 else len(newstr)//2 + 1
        
        for i in range(count+1):
            if newstr[front] != newstr[back]:
                return False
            front += 1
            back -= 1
        return True