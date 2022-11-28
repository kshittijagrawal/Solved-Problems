class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        wl = list(zip(*matches))
        lostZero = set(wl[0])
        lostOne = []
        countLost = Counter(wl[1])
        
        
        for key in countLost.keys():
            if countLost[key] > 0 and key in lostZero:
                lostZero.remove(key)
            if countLost[key] == 1:
                lostOne.append(key)
        
        return [sorted(list(lostZero)),sorted(lostOne)]