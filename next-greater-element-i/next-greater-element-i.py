class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        container, stack = {}, collections.deque()
        for num in nums2:
            while stack and num > stack[-1]:
                container[stack.pop()] = num
            stack.append(num)
        
        print(container)
        return [container.get(num, -1) for num in nums1]