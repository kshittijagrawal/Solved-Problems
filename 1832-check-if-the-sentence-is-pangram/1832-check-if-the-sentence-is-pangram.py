class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s = {a for a in sentence}
        return len(s) == 26