class Solution:
    def square(self,n):
        text = str(n)
        total = 0
        print(text)
        for i in text:
            integer = int(i)
            total += integer**2
        return total
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        tosquare = n
        
        while tosquare != 1:
            number = self.square(tosquare)
            if number in seen:
                return False
            tosquare = number
            seen.add(number)
        return True
            
            
            