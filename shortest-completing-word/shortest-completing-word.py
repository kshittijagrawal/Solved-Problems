class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lplate = {}
        for char in licensePlate:
            if not char.isalpha(): continue
            lplate[char.lower()] = lplate.get(char.lower(), 0) + 1
        
        res = ""
        for word in words:
            lcopy = lplate.copy()
            for char in word:
                if char not in lcopy: continue
                lcopy[char] -= 1
            for val in lcopy.values():
                if val > 0: break
            else:
                if not res or len(word) < len(res):
                    res = word
        return res
            