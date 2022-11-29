class RandomizedSet:

    def __init__(self):
        self.c = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val not in self.c:
            self.arr.append(val)
            self.c[val] = len(self.arr) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.c:
            left = self.c[val]
            right = len(self.arr) - 1
            self.arr[left], self.arr[right] = self.arr[right], self.arr[left]
            self.c[self.arr[left]] = left
            del self.c[self.arr.pop()]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()