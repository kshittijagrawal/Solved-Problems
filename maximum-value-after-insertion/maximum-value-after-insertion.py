class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] != "-":
            i = -1
            for index, char in enumerate(n):
                if int(char) < int(x):
                    i = index
                    break
            return n[:i] + str(x) + n[i:] if i != -1 else n + str(x)
        else:
            i = -1
            for index, char in enumerate(n[1:]):
                if int(char) > int(x):
                    i = index
                    break
            return n[:i+1] + str(x) + n[i+1:] if i != -1 else n + str(x)