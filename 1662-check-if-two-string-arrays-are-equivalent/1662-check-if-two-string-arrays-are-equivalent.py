class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i = j = 0 # character indices
        wi = wj = 0 # word indices
        
        while wi < len(word1) and wj < len(word2):
            if word1[wi][i] == word2[wj][j]:
                i += 1
                j += 1
            else:
                return False
            if i == len(word1[wi]):
                wi += 1
                i = 0
            if j == len(word2[wj]):
                wj += 1
                j = 0
        return wi == len(word1) and wj == len(word2)