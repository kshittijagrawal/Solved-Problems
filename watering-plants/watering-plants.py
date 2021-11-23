class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        c, n, count = capacity, len(plants), 0
        for i in range(n):
            if c < plants[i]:
                count += 2*i
                c = capacity
            c -= plants[i]
        return count + n