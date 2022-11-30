class Solution:
    def secondHighest(self, s: str) -> int:
        con = set()
        for c in s:
            if c.isdigit():
                con.add(int(c))
        
        first = second = -inf
        for num in con:
            if num > first:
                second = first
                first = num
            if num > second and num != first:
                second = num
                
        return second if second != -inf else -1