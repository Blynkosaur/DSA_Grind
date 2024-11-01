class Solution:
    def makeFancyString(self, s: str) -> str:
        new = ''
        count = 1
        previous = None
        for i in range(len(s)):
            
            if s[i]== previous:
                count += 1
            else:
                count = 1
                previous = s[i]
            if count < 3:
                new += s[i]
            

        return new
            