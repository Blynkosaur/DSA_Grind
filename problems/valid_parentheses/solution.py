class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')', "{":'}', '[':']'}
        for i in s:
            if i in dic:
                stack.append(i)
            elif 0 == len(stack) or i != dic[stack.pop()]:
                return False
        return len(stack) == 0
        