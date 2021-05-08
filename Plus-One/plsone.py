class Solution:
    def plusOne(self, digits):
        i,j = 0, len(digits)-1
        while(i<=j):
            if digits[j] == 9:
                digits[j] = 0
            else:
                digits[j] += 1
                break
            j -= 1
        if j >= 0:
            return digits
        digits.insert(0, 1)
        return digits