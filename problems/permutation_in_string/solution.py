class Solution:
    def isValid(self, c1, c2) -> bool:
        for c in c1:
            if c1[c] != c2.get(c, 0):
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = {}
        sub_counter = {}
        if len(s1) > len(s2):
            return False
        for c in s1:
            sub_counter[c]= sub_counter.get(c,0) + 1
        for i in range(len(s1)-1):
            counter[s2[i]] = counter.get(s2[i], 0) + 1
        left = 0
        right = len(s1) - 1 
        for i in range(len(s2) - len(s1) + 1):
            counter[s2[right]] = counter.get(s2[right],0) + 1
            if self.isValid(sub_counter, counter):
                return True
            counter[s2[left]] -= 1
            left += 1
            right += 1
        return False
            
            
            
        