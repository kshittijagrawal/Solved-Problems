class Solution:
    def reformatNumber(self, number: str) -> str:
        count = 0
        res, curr = [], ""
        for c in number:
            if c == " " or c == "-":
                continue
            
            if count == 4:
                res.append(curr[:-1])
                curr = curr[-1]
                count = 1
            count += 1
            curr += c
        
        if count == 4:
            res.append(curr[:2])
            res.append(curr[2:])
        else:
            res.append(curr)
        return "-".join(res)
                