class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        container = collections.Counter(arr)
        res = ""
        for i in range(len(arr)):
            if container[arr[i]] == 1:
                k -= 1
                if k == 0:
                    res = arr[i]
                    break
        return res
            