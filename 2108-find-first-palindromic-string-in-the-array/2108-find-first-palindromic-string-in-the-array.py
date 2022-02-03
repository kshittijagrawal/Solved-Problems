class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res = ""
        for i in range(len(words)):
            n, word = len(words[i]), words[i]
            f, r = 0, n - 1
            for _ in range(n//2):
                if word[f] != word[r]:
                    break
                f, r = f + 1, r - 1
            else:
                res = word
                break
        return res