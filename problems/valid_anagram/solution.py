class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap2 = {}
        for el in s:
            if el not in hashmap:
                hashmap[el]= 0
            hashmap[el] +=1
        for i in t:
            if i not in hashmap2:
                hashmap2[i]=0
            hashmap2[i] += 1
        for i in hashmap2:
            if i not in hashmap:
                return False
            elif hashmap2[i] != hashmap[i]:
                return False
        for i in hashmap:
            if i not in hashmap2:
                return False
            elif hashmap[i] != hashmap2[i]:
                return False
        
        return True
            
            