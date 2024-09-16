class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1)
        ss1 = sorted(s1)
        
        for i in range(len(s2)-len(s1)+1):
            ss2 = s2[left:right]
            ss2 = sorted(ss2)
            if ss1 == ss2:
                return True
            right += 1
            left += 1
        return False