class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, container = collections.deque(), {}
        for num in nums2:
            while stack and stack[-1] < num:
                container[stack.pop()] = num
            stack.append(num)
            
        return [container.get(num, -1) for num in nums1]