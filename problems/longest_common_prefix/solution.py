class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i  = 0
        def check (index:int)->bool:
            for word in strs:
                if index >= len(word):
                    return False
            first = strs[0][i]
            for word in strs:
                if word[index] != first:
                    return False
            return True
        while check(i):
            i += 1
        return strs[0][:i]
        