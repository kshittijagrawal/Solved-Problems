class Solution:
    def minDeletions(self, s: str) -> int:
        container = collections.Counter(s)
        last, res = None, 0
        for key in sorted(container.keys(), key = lambda val : container[val], reverse = True):
            if last == 0:
                res += container[key]
            elif last and container[key] >= last:
                res += (container[key] - last + 1)
                last -= 1
                continue
            else:
                last = container[key]
        return res