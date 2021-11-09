class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def bintodec(s):
            p, r = n - 1, 0
            for i in range(n):
                if s[i] == '1':
                    r += pow(2, p)
                p -= 1
            return r
            
        def dectobin(s):
            r, ind = ["0"] * n, n - 1
            if s == 0: return "".join(r)
            while s > 1:
                r[ind] = str(s % 2)
                s, ind = s // 2, ind - 1
            r[ind] = "1"
            return "".join(r)
            
        n, container = len(nums), set()
        for ind in range(n):
            container.add(bintodec(nums[ind]))
        
        for num in range(pow(2, n)):
            if num not in container:
                return dectobin(num)
        