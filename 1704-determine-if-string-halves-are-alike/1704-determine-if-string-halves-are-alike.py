class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        first = second = 0
        
        for i, char in enumerate(s):
            if i < len(s) // 2:
                first += char in c
            elif i >= len(s) // 2:
                second += char in c
        
        return first == second