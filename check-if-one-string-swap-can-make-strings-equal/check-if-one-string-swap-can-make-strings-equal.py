class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        found = []
        for a, b in zip(s1, s2):
            if a != b:
                found.append(a)
                found.append(b)
                if len(found) > 4: return False

        
        if len(found) == 0: return True
        if len(found) == 2: return False
        return True if found[0] == found[3] and found[1] == found[2] else False