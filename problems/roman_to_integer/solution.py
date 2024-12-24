class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        hashmap = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        prev = 0
        for i in s:
            total += hashmap[i]
            if hashmap[i] > prev:
                total = total - 2*prev
            prev = hashmap[i]
        return total
            