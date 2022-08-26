class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        buckets = [[] for _ in range(11)]
        for i in range(31):
            power_of_two = 1<<i
            digits_count = math.floor(math.log10(power_of_two)) + 1
            buckets[digits_count].append(power_of_two)
        
        n_str_sorted = "".join(sorted(str(n)))
        n_digits_count = math.floor(math.log10(n)) + 1
        for power_of_two in buckets[n_digits_count]:
            if n_str_sorted == "".join(sorted(str(power_of_two))):
                return True
        return False