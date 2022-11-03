class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = collections.Counter(words)
        
        pairs = 0
        evens = odds = 0
        for key in c:
            rev = key[::-1]
            
            if key == rev:
                if c[key] % 2: #odd
                    odds = max(odds, c[key])
                    evens += (c[key] - 1)
                else: #even
                    evens += c[key]
                    
            else:
                pairs += min(c[key], c.get(rev, 0))
                c[key] = 0
        
        if odds:
            evens -= (odds - 1)
        return pairs * 4 + (odds + evens) * 2