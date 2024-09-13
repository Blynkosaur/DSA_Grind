class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        if not s:
            return 0
        if len(s)==1:
            return 1
        maximum = 1
        # print(s[0:0])
        while right < len(s):
            new = s[right] 
            # print(new)
            if new not in s[left:right]:
                right +=1
            else:
                left += 1
            
                
            maximum = max(maximum,right-left)
            print('max',maximum)
        return maximum


        