class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        starttime, maxtime = 0, 0
        arr = [0] * 26
        for t, c in zip(releaseTimes, keysPressed):
            arr[ord(c) - 97] = max(t - starttime, arr[ord(c) - 97])
            maxtime = max(maxtime, arr[ord(c) - 97])
            starttime = t
        
        for i in range(25, -1, -1):
            if arr[i] == maxtime:
                return chr(i + 97)