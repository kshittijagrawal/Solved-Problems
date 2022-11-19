class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {' ': ' '}
        i = 0
        res = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        for char in key:
            if char not in mapping:
                mapping[char] = letters[i]
                i += 1
        
        for char in message:
            res += mapping[char]
                
        return res