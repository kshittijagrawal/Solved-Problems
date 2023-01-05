class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        container, already_present = {}, set()
        
        if len(words) != len(pattern):
            return False
        
        for p, word in zip(pattern, words):
            if container.get(p):
                if container[p] != word:
                    return False
            else:
                if word in already_present:
                    return False
                container[p] = word
                already_present.add(word)
            
        return True