class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        fpow, res = 0, set()
        if x<y: x, y = y, x
            
        while x**fpow <= bound:
            spow, fcurr = 0, x**fpow
            while fcurr+(y**spow) <= bound:
                res.add(fcurr+(y**spow))
                spow += 1
                if y == 1:break
            fpow += 1
            if x == 1:
                break
        return res