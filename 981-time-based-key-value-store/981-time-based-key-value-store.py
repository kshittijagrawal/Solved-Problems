class TimeMap:

    def __init__(self):
        self.structure_value = {}
        self.structure_time = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.structure_value.setdefault(key, []).append(value)
        self.structure_time.setdefault(key, []).append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        lo, hi = 0, len(self.structure_time.get(key, [])) - 1
        mid = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.structure_time[key][mid] == timestamp:
                break
            elif self.structure_time[key][mid] > timestamp:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            mid = lo - 1
        return self.structure_value[key][mid] if mid >= 0 else ""
                
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)