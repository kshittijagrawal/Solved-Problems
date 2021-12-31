class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num != 0 and num % 10 == 0:
            return False
        return True