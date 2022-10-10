class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        c = {a: b for a, b in paths}
        for key in c:
            if not c.get(c[key], 0):
                return c[key]