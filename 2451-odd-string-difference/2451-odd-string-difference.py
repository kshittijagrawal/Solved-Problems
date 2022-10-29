class Solution:
    def oddString(self, words: List[str]) -> str:
        a = b = None
        for word in words:
            diff = []
            for i in range(1, len(word)):
                diff.append(ord(word[i]) - ord(word[i - 1]))
            if not a:
                a = diff
            elif not b:
                b = diff
            else:
                if a == b:
                    if diff != a:
                        return word
                else:
                    return words[0] if diff == b else words[1]
                
                