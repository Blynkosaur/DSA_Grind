class Solution:
    def characterReplacement(self,s: str, k: int) -> int:
        left = 0 
        right = 0
        maximum = 0
        hashmap = {s[left]:0}
        popular =1
        while right < len(s):
            
            
                
            if s[right] not in hashmap:
                hashmap[s[right]] = 1
            else:
                hashmap[s[right]] += 1
            popular  = max(hashmap.values())
            if (right-left+1)- popular > k:
                hashmap[s[left]] -= 1
                left += 1

            maximum = max(maximum, right-left+1)
                
            
            right += 1
        
        
        return maximum