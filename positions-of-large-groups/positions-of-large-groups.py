class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        start = end = 0
        res = []
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                end += 1
            else:
                if end - start + 1 >= 3:
                    res.append([start, end])
                start = end = i
        if end - start + 1 >= 3: res.append([start, end])
            
        return res