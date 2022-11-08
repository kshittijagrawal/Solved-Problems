class Solution:
    def makeGood(self, s: str) -> str:
        st = []
        
        for c in s:
            if st and abs(ord(st[-1]) - ord(c)) == 32:
                st.pop()
            else:
                st.append(c)
                
        return "".join(st)