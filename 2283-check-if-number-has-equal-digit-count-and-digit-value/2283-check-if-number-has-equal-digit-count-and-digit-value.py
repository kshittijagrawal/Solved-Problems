class Solution:
    def digitCount(self, num: str) -> bool:
        container = {}
        
        for d in num:
            container[d] = container.get(d, 0) + 1
        
        for i in range(len(num)):
            if container.get(str(i), 0) != int(num[i]):
                return False
        return True