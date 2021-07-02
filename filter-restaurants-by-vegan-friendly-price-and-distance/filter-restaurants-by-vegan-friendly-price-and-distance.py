class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        container = {}
        for i, r, v, p, d in restaurants:
            if veganFriendly:
                if not v: continue
            if p<=maxPrice and d<=maxDistance:
                container[i] = r
        
        container = sorted(container.items(), key = lambda x: (-x[1], -x[0]))
        return [i for i, r in container]