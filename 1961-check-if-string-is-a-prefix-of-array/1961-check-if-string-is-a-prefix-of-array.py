class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        ss = se = 0
        l = len(s)
        for word in words:
            se += len(word)
            if s[ss:se] != word:
                return False
            ss = se
            if ss == l: return True
        return False