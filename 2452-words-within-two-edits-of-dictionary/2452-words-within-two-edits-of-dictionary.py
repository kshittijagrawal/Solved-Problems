class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        for q in queries:
            for w in dictionary:
                count = 0
                for c, d in zip(w, q):
                    if c != d:
                        count += 1
                        if count > 2:
                            break
                else:
                    res.append(q)
                    break
        return res