class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1 = {c : 1 for c in "qwertyuiop"}
        line2 = {c : 2 for c in "asdfghjkl"}
        line3 = {c : 3 for c in "zxcvbnm"}
        lines = line1 | line2 | line3
        res = []
        
        for word in words:
            line = lines[word[0].lower()]
            for i in range(1, len(word)):
                if lines[word[i].lower()] != line:
                    break
            else:
                res.append(word)
        return res
                