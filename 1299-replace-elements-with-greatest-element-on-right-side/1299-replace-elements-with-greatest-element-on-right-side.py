class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = arr[-1]
        for i in range(len(arr) - 1, 0, -1):
            prev = arr[i - 1]
            arr[i - 1] = max(curr, arr[i])
            curr = max(curr, prev)
        arr[-1] = -1
        return arr