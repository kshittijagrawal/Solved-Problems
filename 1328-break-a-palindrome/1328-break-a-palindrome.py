class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        
        res, flag = [palindrome[n // 2]] * n, 0
        for i in range(n // 2):
            if not flag and palindrome[i] != 'a':
                res[i] = 'a'
                flag = 1
            else:
                res[i] = palindrome[i]
            res[n - i - 1] = palindrome[i]
        if not flag:
            res[-1] = "b"
        return "".join(res)