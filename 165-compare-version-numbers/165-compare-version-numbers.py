class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = v2 = 0
        vl1, vl2 = len(version1), len(version2)
        while v1 < vl1 or v2 < vl2:
            vn1 = 0
            while v1 < vl1 and version1[v1] != ".":
                vn1 = vn1*10 + int(version1[v1])
                v1 += 1
            vn2 = 0
            while v2 < vl2 and version2[v2] != ".":
                vn2 = vn2*10 + int(version2[v2])
                v2 += 1
            if vn1 > vn2:
                return 1
            if vn1 < vn2:
                return -1
            v1, v2 = v1 + 1, v2 + 1
        return 0
            