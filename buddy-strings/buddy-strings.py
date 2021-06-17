class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        # if strings are equal, for being a "buddy string" they have to contain atleast one duplicate
        if s == goal:
            if len(s) >= len(set(s))+1:
                return True
            return False
            
        found = []
        for scurr, gcurr in zip(s, goal):
            if len(s) == 1: return False
            if scurr != gcurr:
                if len(found) > 2: return False
                if len(found) == 2:
                    if found[1] != scurr or found[0] != gcurr: return False
                found.append(scurr)
                found.append(gcurr)
        return True if len(found) != 2 else False
