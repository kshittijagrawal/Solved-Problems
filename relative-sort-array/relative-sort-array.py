class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        container = collections.Counter(arr1)
        ind = 0
        for num in arr2:
            count = container.get(num)
            while count:
                arr1[ind] = num
                ind, count = ind+1, count-1
            del container[num] # constant time operation
        
        rem = sorted(container)
        for num in rem:
            count = container[num]
            while count:
                arr1[ind] = num
                ind, count = ind+1, count-1
        
        return arr1