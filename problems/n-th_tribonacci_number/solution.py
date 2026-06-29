class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [0,1,1]
        if n < 3:
            return trib[n]
        curr = 3
        for i in range(n-2):
            trib.append(trib[curr-1]+trib[curr-2]+trib[curr-3])
            curr += 1
        return trib[n]
        