class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split()
        ls = ls[::-1]
        ret = ''
        for i in ls:
            ret += i
            ret += " "
        return ret[:-1]