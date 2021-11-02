class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev, res = s[0], 0
        pc, cc, flag = 1, 0, 0
        
        for i in range(1, len(s)):
            if s[i] == prev:
                if flag:
                    prev = '0' if prev == '1' else '1'
                    res += min(pc, cc)
                    pc, cc= cc, 1
                else:
                    pc += 1
            else:
                cc, flag = cc + 1, 1
            
        return res + min(pc, cc)
    