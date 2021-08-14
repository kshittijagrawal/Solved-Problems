class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for s in strs:
            key = frozenset(Counter(s).items())
            d[key].append(s)
        return d.values()