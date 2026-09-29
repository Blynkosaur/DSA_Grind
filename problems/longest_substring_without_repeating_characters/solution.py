class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        longest = 0
        curr = 0
        for i in range(len(s)):
            last_seen = hashmap.get(s[i], None) 

            if last_seen is not None and last_seen >= curr:
                longest = max(longest,i - curr)
                curr = last_seen+1

            hashmap[s[i]] = i
            
        longest = max(longest, len(s)-curr)
        return longest
                 

        