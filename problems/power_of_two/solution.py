class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        power  = 1
        while power < n:
            power *= 2
            if power == n:
                return True
        return False
