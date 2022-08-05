class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        my = s.split()
        return len(my[-1])