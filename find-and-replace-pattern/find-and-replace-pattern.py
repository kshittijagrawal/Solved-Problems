class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        for word in words:
            wdict, alreadypresent = {}, set()
            for w, p in zip(word, pattern):
                if p in wdict:
                    if wdict[p] != w:
                        break
                else:
                    if w in alreadypresent:
                        break
                    wdict[p] = w
                alreadypresent.add(w)
            else:
                res.append(word)
        return res