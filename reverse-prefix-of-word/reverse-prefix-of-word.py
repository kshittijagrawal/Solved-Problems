class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        arr = collections.deque()
        
        for i in range(len(word)):
            arr.appendleft(word[i])
            if word[i] == ch:
                return "".join(arr) + word[i+1:]
        
        else:
            return word
        
            
        
        