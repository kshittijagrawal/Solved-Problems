class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split()
        if len(slist) != len(pattern):
            return False
        
        match, alreadymapped = {}, set()
        for current in zip(pattern, slist):
            if current[0] not in match:
                if current[1] in alreadymapped:
                    return False
                match[current[0]] = current[1]
            else:
                if current[1] != match[current[0]]:
                    return False
            alreadymapped.add(current[1])
            
        return True