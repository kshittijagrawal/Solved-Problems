class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        counter = collections.Counter(candyType)
        thismany = len(candyType)//2
        return min(thismany, len(counter.keys()))
        
        