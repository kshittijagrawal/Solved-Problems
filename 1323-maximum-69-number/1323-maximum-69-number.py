class Solution:
    def maximum69Number (self, num: int) -> int:
        count, sixpos = 0, -1
        n = num
        while n > 0:
            if n % 10 == 6:
                sixpos = count
            count += 1
            n //= 10
        
        factor = 10 ** sixpos
        if sixpos >= 0:
            return (num // factor + 3) * factor + (num % factor)
        return num