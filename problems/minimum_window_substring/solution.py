class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        
        tHash = {}
        for char in t:
            tHash[char] = tHash.get(char, 0) + 1
        
        required = len(tHash)
        windowCounts = {}
        have = 0
        start = 0
        result = (float('inf'), 0, 0)  # (window length, left, right)
        
        for end in range(len(s)):
            char = s[end]
            windowCounts[char] = windowCounts.get(char, 0) + 1
            
            if char in tHash and windowCounts[char] == tHash[char]:
                have += 1
            
            while have == required:
                if (end - start + 1) < result[0]:
                    result = (end - start + 1, start, end)
                
                windowCounts[s[start]] -= 1
                if s[start] in tHash and windowCounts[s[start]] < tHash[s[start]]:
                    have -= 1
                start += 1
        
        return s[result[1]:result[2]+1] if result[0] != float('inf') else ''