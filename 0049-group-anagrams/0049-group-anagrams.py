class Solution:
    def groupAnagrams(self, strs):
        container = {}
        for str in strs:
            d = collections.Counter(str)
            container.setdefault(frozenset(d.items()), []).append(str)
        
        return [container[key] for key in container]