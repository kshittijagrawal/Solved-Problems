class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = collections.Counter(allowed)
        count = 0
        
        for word in words:
            flag = 0
            word = set(word)
            for char in word:
                if char not in counter:
                    flag = 1
                    break
            if flag == 0:
                count += 1
        
        return count