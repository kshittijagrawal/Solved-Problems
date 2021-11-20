class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res, first, last, curr = [0] * len(s), 0, None, 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                curr, first = 1, i
                last = first if not last else last
            else:
                res[i] = curr
                curr += 1
        
        curr = 1
        for i in range(first + 1, last):
            if s[i] == c:
                curr = 1
            else:
                res[i] = min(res[i], curr)
                curr += 1
        
        for i in range(last + 1, len(s)):
            res[i] = i - last
                
        return res