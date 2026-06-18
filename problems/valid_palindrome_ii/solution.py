class Solution:
    def validPalindrome(self, s: str) -> bool:
        chance = True
        left = 0 
        right = len(s) -1
        while left < right:
            if s[left] != s[right]:
                if chance: # allowed to skip one letter
                    if s[left+1] == s[right] and s[left] == s[right-1]:
                        left += 1
                        right -=1
                        continue
                    elif s[left+1] == s[right]:
                        left+=1
                    elif s[left] == s[right-1]:
                        right-=1
                    else:
                        return False
                    chance = False

                else:
                    return False
            else:
                left += 1
                right -=1
        return True
    

                
                


        