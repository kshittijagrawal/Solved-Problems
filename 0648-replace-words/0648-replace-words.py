class TrieNode:
    def __init__(self):
        self.child = {}
        self.lastWord = False
        
class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if cur.child.get(c, None) is None:
                cur.child[c] = TrieNode()
            cur = cur.child[c]
        cur.lastWord = True
         
    def startsWith(self, prefix):
        cur = self.root
        res = ""
        for c in prefix:
            if cur.child.get(c, None) is None:
                if cur.lastWord:
                    return res
                else:
                    return ""
            else:
                if cur.lastWord:
                    return res
            res+=c
            cur = cur.child[c]
        return res
    
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            self.insert(word)
        ans = []
        for word in sentence.split(' '):
            res = self.startsWith(word)
            if not res:
                ans.append(word)
            else:
                ans.append(res)
        return " ".join(ans)