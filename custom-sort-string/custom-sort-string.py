class Solution:
    def customSortString(self, order: str, string: str) -> str:
        counter = collections.Counter(string)
        res = ""
        for i in order:
            if i in string:
                res += i * (counter[i])
                string = string.replace(i, "")
        
        return res+string
                