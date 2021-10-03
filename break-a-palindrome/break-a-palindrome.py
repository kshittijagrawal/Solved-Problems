class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        if length == 1:
            return ""
        
        arr = list(map(str, palindrome))
        limit = length // 2 if length%2 == 0 else (length - 1) // 2
        
        for i in range(limit):
            if arr[i] != 'a':
                arr[i] = 'a'
                break
        else:
            arr[-1] = 'b'
        
        return "".join(arr)