class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        s = str(x)[::-1]
        if int(s) == x:
            return True
        return False