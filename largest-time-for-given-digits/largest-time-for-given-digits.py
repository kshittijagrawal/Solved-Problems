class Solution:    
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans = ''
        for i, a in enumerate(A):
            for j, b in enumerate(A):
                for k, c in enumerate(A):
                    if i == j or i == k or j == k:
                        continue
                    hour, minute = str(a) + str(b), str(c) + str(A[6 - i - j - k])
                    if hour < '24' and minute < '60':
                        ans = max(ans, hour + ':' + minute)
        return ans