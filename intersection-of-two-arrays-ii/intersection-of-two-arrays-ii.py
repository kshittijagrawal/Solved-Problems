class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        container, res = {}, []
        for num in nums1:
            container[num] = container.get(num, 0) + 1
        
        for num in nums2:
            if container.get(num, 0):
                res.append(num)
                container[num] -= 1
        
        return res