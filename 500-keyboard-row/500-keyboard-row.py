class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lines = {c : 1 for c in "qwertyuiop"} | {c : 2 for c in "asdfghjkl"} | {c : 3 for c in "zxcvbnm"}
        res = []
        
        for word in words:
            line = lines[word[0].lower()]
            for i in range(1, len(word)):
                if lines[word[i].lower()] != line:
                    break
            else:
                res.append(word)
        return res
                