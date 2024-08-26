import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+","-","*","/"]
        for el in tokens:
            if el not in ops:
                stack.append(el)
            elif el in ops:
                two = stack.pop()
                one = stack.pop()
                op = one+el+two
                # print(op)
                answer = eval(op)
                answer = math.trunc(answer)
                
                stack.append(str(answer))
        
        return int(stack[0])