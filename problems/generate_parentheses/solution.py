class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = ['(']
        answer = []
        while stack:
            el = stack.pop(0)
            if len(el) == n*2:
                answer.append(el)
            else:
                if el.count("(")< n:
                    op = el + "("
                    stack.append(op)
                if el.count("(") > el.count(")"):
                    cl = el + ")"
                    stack.append(cl)
        return answer
            
