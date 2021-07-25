class Solution:
    def compress(self, chars: List[str]) -> int:
        ind, curchar, curcount = 0, chars[0], 1
        for char in chars[1:]:
            if char == curchar:
                curcount += 1
            else:
                chars[ind] = curchar
                ind += 1
                if curcount >= 2:
                    for c in str(curcount):
                        chars[ind] = c
                        ind += 1
                curcount, curchar = 1, char
        chars[ind] = curchar
        ind += 1
        if curcount >= 2:
            for c in str(curcount):
                chars[ind] = c
                ind += 1
        return ind