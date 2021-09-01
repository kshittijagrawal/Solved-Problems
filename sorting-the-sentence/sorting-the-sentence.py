class Solution:
    def sortSentence(self, s: str) -> str:
        container, word = {}, ""
        for c in s:
            if c == " ": continue 
            if c.isdigit():
                container[int(c)] = word
                word = ""
            else:
                word += c
        
        res = ""
        for i in range(1, 10):
            if container.get(i, 0):
                res += container.get(i)
                res += " "
        
        return res[:-1]