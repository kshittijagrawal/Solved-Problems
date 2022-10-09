class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            if carry:
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += carry
                    carry = 0
        if carry:
            digits = [1] + digits
        return digits