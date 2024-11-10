class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        power = 1
        while power < n:
            power *= 4
            if power == n:
                return True
        return False