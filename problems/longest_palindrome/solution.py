class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        lenght = 0
        for i in s:
            if i not in hashmap:
                hashmap[i]= 0
            hashmap[i]+=1
        
        print(hashmap)
        for i in hashmap:
            lenght += int((hashmap[i]/2))*2
            if lenght%2 == 0 and hashmap[i]%2 ==1:
                lenght +=1
            
        
        
        return lenght