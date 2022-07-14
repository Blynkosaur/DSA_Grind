class Solution:
    def isPalindrome(self, s: str) -> bool:
        mylist = []
        abc = "a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9"
        new = s.lower()
        valid = abc.split(" ")
        
        
        for el in new:
            
            if el in valid:
                mylist.append(el)
        reversedlist = []
        copy = []
        for i in mylist:
            copy.append(i)
        for i in range(len(mylist)):
            reversedlist.append(mylist[-1])
            mylist.pop(-1)
        print(copy)
        
        print(reversedlist)
        if reversedlist == copy:
            return True
        return False