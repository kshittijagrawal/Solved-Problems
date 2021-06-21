class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        tocheckwith, res = folder[0], []
        res.append(tocheckwith)
        for f in folder[1:]:
            if f[:len(tocheckwith)+1] != tocheckwith+"/":
                res.append(f)
                tocheckwith = f
        return res