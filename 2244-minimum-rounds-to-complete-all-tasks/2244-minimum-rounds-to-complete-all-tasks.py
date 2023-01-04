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
            if r3 == 0: #for nums perfectly dividing 3
                res += t3
            
            else: #for nums producing remainders 1 and 2
                res += t3 + 1

            
        return res