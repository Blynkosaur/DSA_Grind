class Solution:
    def isValid(self, s: str) -> bool:
        hash = {")":"(","]":"[","}":"{"}
        stack  = []
        for el in s:
            
            
            if el not in hash:
                stack.append(el)
            elif el in hash:
                if hash[el] not in stack:
                    return False
                
                elif stack.pop() != hash[el]:
                    
                    return False
        if len(stack)== 0:
            return True
            
        