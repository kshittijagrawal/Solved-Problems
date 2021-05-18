class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, _max = 0, 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                _max = max(_max, 2*right)
            else:
                if right >= left:
                    left = 0
                    right = 0
        
        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                _max = max(_max, 2*left)
            else:
                if left >= right:
                    left = 0
                    right = 0
        return _max