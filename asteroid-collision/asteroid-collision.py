class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = collections.deque()
        for a in asteroids:
            while stack and stack[-1] > 0 and a < 0:
                f, s = abs(stack[-1]), abs(a)
                if f < s:
                    stack.pop()
                    continue
                elif f == s:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack