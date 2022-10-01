class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        res = i = 0
        while i < len(sentence):
            swi = 0
            
            while swi < len(searchWord) and i < len(sentence):
                if searchWord[swi] != sentence[i]: break
                swi, i = swi + 1, i + 1
            else: return res + 1
            
            while i < len(sentence) and sentence[i] != " ": i += 1
            i, res = i + 1, res + 1
            
        return -1