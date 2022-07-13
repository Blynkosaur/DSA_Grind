class Solution:
    def isValid(self, s: str) :
        hashmap = {"(":")","{":"}","[":"]"}
        opened = []
        for i in range(len(s)):
            if s[i] in hashmap:
                opened.append(s[i])
            else:
                if len(opened) !=0:
                    if hashmap[opened[-1]]== s[i] :
                        flag = True
                        opened.pop(-1)
                    else:
                        return False
                else:
                    return False
        if len(opened) != 0:
            return False
        
            
        
            
        return flag
                
            