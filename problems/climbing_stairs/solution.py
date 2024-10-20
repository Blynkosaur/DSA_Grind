class Solution:
    def climbStairs(self, n: int) -> int:
        hashmap = {1:1,2:2}
        if n == 1:
            return 1
        elif n ==2:
            return 2
        else: 
            for i in range(3,n+1):
                hashmap[i] = hashmap[i-1]+hashmap[i-2]

        return hashmap[n]
