class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = {5:0, 10:0, 20:0}
        for bill in bills: 
            change = bill - 5
            if change == 5:
                if register[5] == 0:
                    return False
                else:
                    register[5] -= 1
            elif change == 15:
                if register[10] != 0 and register[5] != 0:
                    register[10] -=1
                    register[5] -= 1
                elif register[5] >= 3:
                    register[5] -= 3
                else:
                    return False
            register[bill] += 1
        return True

                
            
    
        