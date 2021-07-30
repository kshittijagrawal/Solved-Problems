import math
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evenplaces = n // 2 if n % 2 == 0 else n // 2 + 1
        return (pow(5, evenplaces, 1000000007) * pow(4, n-evenplaces, 1000000007)) % 1000000007