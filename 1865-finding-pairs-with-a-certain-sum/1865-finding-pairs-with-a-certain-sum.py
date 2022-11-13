class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.c = collections.Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        # print(f"add called with {index} and {val}")
        
        self.c[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.c[self.nums2[index]] = self.c.get(self.nums2[index], 0) + 1
        
        # print(f"updated nums2 = {self.nums2}\nupdated c = {self.c}")

    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            if tot - num in self.c:
                res += self.c[tot - num]
        
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)