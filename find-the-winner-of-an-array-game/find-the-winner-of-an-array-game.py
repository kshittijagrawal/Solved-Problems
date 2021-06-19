class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        candidate, count = arr[0], 0
        for num in arr[1:]:
            if candidate > num:
                count += 1
            else:
                candidate, count = num, 1
            if count == k:
                return candidate
        return candidate