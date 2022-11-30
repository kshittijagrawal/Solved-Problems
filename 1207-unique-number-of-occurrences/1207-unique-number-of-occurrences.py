class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c1 = collections.Counter(arr)
        c2 = set()
        for num in arr:
            c2.add(c1[num])
        return len(c1) == len(c2)