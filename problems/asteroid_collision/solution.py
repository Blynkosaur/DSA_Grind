class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ass in asteroids:
            if ass > 0:
                stack.append(ass)
            else:
                add_new = True
                while stack and stack[-1] > 0:
                    if abs(stack[-1]) < abs(ass):
                        stack.pop()
                    elif abs(stack[-1]) > abs(ass):
                        add_new = False
                        break
                    else:
                        add_new = False
                        stack.pop()
                        break
                if add_new:
                    stack.append(ass)
        return stack
                    