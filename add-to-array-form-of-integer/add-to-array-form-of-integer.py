class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        length, number = len(num)-1, 0
        for n in num:
            number += n*10**length
            length -= 1
        
        number += k
        length = len(str(number))
        res = [0]*length
        for i, c in enumerate(str(number)):
            res[i] = int(c)
        return res