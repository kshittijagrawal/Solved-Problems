class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        container, n = collections.Counter(arr), len(arr)
        freqs = sorted(container.items(), key = lambda x: -x[1])
        halflength, res = n//2, 0
        
        for _, freq in freqs:
            res += 1
            n -= freq
            if n <= halflength:
                break
        return res