class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        flag = 1 if flowerbed[0] == 0 else 0
        for i in range(length):
            if flag == 1 and flowerbed[i] == 0 and (i == length-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1 
            flag = 1 if flowerbed[i] == 0 else 0
            if n <= 0:
                return True
        return False