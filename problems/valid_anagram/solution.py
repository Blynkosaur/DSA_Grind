class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ls = []
        t_ls = []
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            

            s_ls.append(s[i])
            t_ls.append(t[i])
            
            
        
        s_s = sorted(s_ls)
        t_s = sorted(t_ls)
        print(s_s)
        print(t_s)
        if s_s == t_s:
            return True
        else:
            return False


        