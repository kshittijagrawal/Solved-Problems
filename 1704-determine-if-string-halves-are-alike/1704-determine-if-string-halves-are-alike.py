class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        first = second = 0
        
        for i, char in enumerate(s):
            if i < len(s) // 2 and char in c:
                first += 1
            elif i >= len(s) // 2 and char in c:
                second += 1
        
        return first == second