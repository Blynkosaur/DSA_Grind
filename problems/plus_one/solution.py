class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = ''
        for dig in digits:
            number += str(dig)
        summ = str(int(number)+1)
        ret = []
        for i in summ:
            ret.append(int(i))
        return ret