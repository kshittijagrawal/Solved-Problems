class Solution:
    def addDigits(self, num: int) -> int:
        #solution using constant time and space
        if num == 0:
            return 0
        elif num%9 == 0:
            return 9
        else:
            return num%9