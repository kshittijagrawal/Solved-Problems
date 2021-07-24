class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        container = {key:val for key, val in knowledge}
        res, temp, flag = "", "", 0
        for c in s:
            if c == ")":
                res += container.get(temp, "?")
                flag, temp = 0, ""
            elif c == "(" or flag == 1:
                if flag == 1:
                    temp += c
                else:
                    flag = 1
            else:
                res += c
        return res