class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomMap ={}
        ransomMag ={}
        for i in ransomNote:
            if i not in ransomMap:
                ransomMap[i] = 0
            ransomMap[i] += 1
        for i in magazine:
            if i not in ransomMag:
                ransomMag[i] = 0
            ransomMag[i] += 1
        for i in ransomMap:
            if i not in ransomMag:
                return False
            else:
                if ransomMap[i]> ransomMag[i]:
                    return False
        return True
