class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = collections.Counter(stones)
        j = set(jewels)
        res = 0
        for k in s.keys():
            if k in j:
                res += s[k]
        return res