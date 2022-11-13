class Solution:
    def reverseWords(self, s: str) -> str:
        res, word = [], collections.deque()
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if word:
                    res.append("".join(word))
                    word = collections.deque()
            else:
                word.appendleft(s[i])
        
        if word: res.append("".join(word))
        return " ".join(res)
        