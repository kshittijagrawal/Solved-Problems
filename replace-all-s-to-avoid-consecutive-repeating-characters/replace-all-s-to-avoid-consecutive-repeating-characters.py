class Solution:
    def modifyString(self, s: str) -> str:
        if len(s)==1:
            return 'a' 
        s=list(s)
        for i in range(len(s)):
            if s[i] == '?':
                for x in 'abc':                
                    if i == 0  and s[i+1] != x: 
                        s[i]=x
                    elif i != 0 and i+1 != len(s):
                        if s[i+1] != x and s[i-1] != x:
                            s[i]=x                            
                    elif i==len(s)-1 and s[i-1] != x:
                        s[i]=x
        return ''.join(s)