class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        one_ptr = 0 
        two_ptr = 0
        alt = True
        while one_ptr < len(word1) and two_ptr < len(word2):
            if alt:
                output += word1[one_ptr]
                one_ptr += 1
            else:
                output += word2[two_ptr]
                two_ptr += 1
            alt = not alt
        if one_ptr < len(word1):
            output += word1[one_ptr:]
        else:
            output += word2[two_ptr:]
        return output

        