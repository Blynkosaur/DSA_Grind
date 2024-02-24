class Solution:
    def addDigits(self,num):
        def hehe(num):
            n = str(num)
            ls = [x for x in n]
            intls = [int(x) for x in ls]
            answer = sum(intls)
            if len(str(answer))> 1:
                answer = hehe(answer)
            else:
                answer = answer
            return answer
        return hehe(num)