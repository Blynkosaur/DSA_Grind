class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        init = [1]
        def pascal(array):
            ret = [1]
            for i in range(1,len(array)):
                ret.append(array[i]+array[i-1])
            ret.append(1)
            return ret
        for i in range(rowIndex):
            init = pascal(init)
        return (init)