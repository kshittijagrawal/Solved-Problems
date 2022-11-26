class Solution:
    def solveEquation(self, equation: str) -> str:
        def evaluate(expression):
            tokens = expression.replace("+", "#+").replace("-", "#-").split("#")  # For example: "x+5-3+x" is replaced to "x#+5#-3#+x" then split by "#"
            res = [0] * 2
            for token in tokens:
                if not token: continue
                if token == "x" or token == "+x":
                    res[0] += 1
                elif token == "-x":
                    res[0] -= 1
                elif "x" in token:
                    res[0] += int(token[:token.index("x")])
                else:
                    res[1] += int(token)
            return res

        parts = equation.split("=")
        leftRes = evaluate(parts[0])
        rightRes = evaluate(parts[1])
        a = leftRes[0] - rightRes[0]
        b = rightRes[1] - leftRes[1]
        if a == 0 and b == 0:
            return "Infinite solutions"
        if a == 0:
            return "No solution"
        return "x={}".format(b // a)