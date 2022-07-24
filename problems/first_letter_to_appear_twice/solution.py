class Solution:
    def repeatedCharacter(self, s: str) -> str:
        hashmap = {}
        for el in s:
            if el not in hashmap:
                hashmap[el]=0
            hashmap[el]+=1
            if hashmap[el]>1:
                return el
            