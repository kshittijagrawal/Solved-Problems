class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        match, alreadymapped = {}, set()
        for current in zip(s, t):
            if current[0] not in match:
                if current[1] in alreadymapped:
                    return False
                match[current[0]] = current[1]
            else:
                if current[1] != match[current[0]]:
                    return False
            alreadymapped.add(current[1])
        return True