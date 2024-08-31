class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        left = 0
        s = s.lower()
        new = ""
        for i in s:
            if i.isalnum():
                new +=i
        right = len(new)-1
        while right> left:
            if new[left] != new[right]:
                return False
            left += 1
            right -= 1
        return True