class Solution:
    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        if len(s2) > len(s1): s1, s2 = s2, s1
        if s1 == s2: return True
        
        arr1, arr2 = collections.deque(s1.split()), collections.deque(s2.split())
        while arr1 and arr2:
            if arr1[0] == arr2[0]:
                arr1.popleft()
                arr2.popleft()
            elif arr1[-1] == arr2[-1]:
                arr1.pop()
                arr2.pop()
            else:
                break
        else:
            return True if not len(arr2) else False
        return False

        
            