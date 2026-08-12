class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        
        def backtrack(p, opened, curr):
            if len(p) == n * 2:
                output.append(p)
                return
            if opened < n:
                backtrack(p + "(", opened + 1, curr + 1)
            if curr > 0:
                backtrack(p + ")", opened, curr - 1)
        backtrack("", 0, 0)
        return output
        
        