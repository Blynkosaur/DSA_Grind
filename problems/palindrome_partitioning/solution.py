class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(st):
            l, r = 0, len(st)-1
            while l < r:
                if st[l] != st[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        sols = []
        n = len(s)
        def backtrack(i,ls):
            if i == n:
                sols.append(ls.copy())
                return
            for j in range(i, n):
                if is_palindrome(s[i:j+1]):
                    ls.append(s[i:j + 1])
                    backtrack(j+1,ls)
                    ls.pop()
                
        backtrack(0,[])
        return sols
        