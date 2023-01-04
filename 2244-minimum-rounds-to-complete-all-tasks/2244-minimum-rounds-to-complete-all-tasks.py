class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        container = {}
        for task in tasks:
            container[task] = container.get(task, 0) + 1
        
        res = 0
        # print(container)
        for key in container:
            if container[key] == 1:
                return -1
            
            t3, r3 = divmod(container[key], 3)
            if r3 == 0:
                res += t3
            
            if r3 == 1:
                res += t3 + 1
            
            if r3 == 2:
                res += t3 + 1
            
        return res