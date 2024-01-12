class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        stringls = []
        for l in x:
            stringls.append(l)
        if stringls == stringls[::-1]:
            return True
        return False