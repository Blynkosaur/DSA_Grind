class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = list(s)
        left = 0
        right =1
        maxlenght = 0
        print(string[left:right])
        if len(s)==0:
            return 0
        elif len(s)==1:
            return 1
        while right != len(string):
            if string[right] not in string[left:right]:
                right += 1
            else:
                left +=1
            if right - left >maxlenght:
                maxlenght = right- left
        return maxlenght