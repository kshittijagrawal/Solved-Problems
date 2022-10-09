class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {}
        
        for b in bills:
            
            if b == 10:
                if change.get(5,0): change[5] -= 1
                else: break
                    
            if b == 20:
                if change.get(10,0) and change.get(5,0):
                    change[10] -= 1
                    change[5] -= 1
                elif change.get(5,0) > 2:
                    change[5] -= 3
                else: break
                
            change[b] = change.get(b, 0) + 1
            
        else:
            return True
        return False