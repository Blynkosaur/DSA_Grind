class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x *= -1
        mystring = str(x)
        mylist = []
        for i in mystring:
            mylist.append(i)
        
        
        mylist.reverse()
        final = ''
        for i in mylist:
            final += i
        finalInt = int(final)
        if negative == True:
            finalInt  = finalInt* -1
        if finalInt > 2**31 -1 or finalInt<-2**31:
            finalInt = 0
        
            
        return finalInt
        
        