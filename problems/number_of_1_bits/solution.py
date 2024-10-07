class Solution:
    def hammingWeight(self, n: int) -> int:
        binn = bin(n)
        print(str(binn))
        numb = 0
        for el in str(binn):
            if el == '1':
                numb += 1
        return numb