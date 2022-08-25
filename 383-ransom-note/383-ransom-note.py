class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = collections.Counter(magazine)
        for i in range(len(ransomNote)):
            if c.get(ransomNote[i], 0):
                c[ransomNote[i]] -= 1
                continue
            return False
        return True 