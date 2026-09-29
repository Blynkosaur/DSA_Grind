class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        curr = 0
        maxf = 0
        hashmap = {s[0]:1}
        for i in range(1,len(s)):
            hashmap[s[i]] = hashmap.get(s[i],0) + 1
            maxf = max(maxf, hashmap[s[i]])

            while i - curr + 1 - maxf > k:
                hashmap[s[curr]] -= 1
                curr += 1
            
            longest = max(longest, i - curr + 1)
        longest = max(longest, len(s) - curr)
            
            
        return longest
                    
                
                
            
            
            

        