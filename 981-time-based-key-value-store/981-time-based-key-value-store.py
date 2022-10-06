class TimeMap:

    def __init__(self):
        self.s_v = {}
        self.s_t = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.s_v.setdefault(key, []).append(value)
        self.s_t.setdefault(key, []).append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        lo, hi = 0, len(self.s_t.get(key, [])) - 1
        mid = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.s_t[key][mid] == timestamp: break
            elif self.s_t[key][mid] > timestamp: hi = mid - 1
            else: lo = mid + 1
        else:
            mid = lo - 1
        return self.s_v[key][mid] if mid >= 0 else ""
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)