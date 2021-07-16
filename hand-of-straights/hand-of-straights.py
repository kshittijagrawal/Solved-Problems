class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False
        
        container, hand = collections.Counter(hand), sorted(hand)
        index = 0
        
        while index < n:
            curr = hand[index]
            for i in range(groupSize):
                if not container.get(curr+i, 0):
                    return False
                container[curr+i] -= 1
                if not container[curr+i]:
                    del container[curr+i]
            
            index += 1
            while index<n and not container.get(hand[index], 0):
                index += 1
        
        return True