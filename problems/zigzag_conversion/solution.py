class Solution:
    def convert(self, s: str, numRows: int) -> str:
        listedS = list(s)
        addition = True
        counter = 0
        thicc_container = [ [] for _ in range(numRows) ]

        if numRows == 1:
            return s
        
        for e in listedS:
            
            thicc_container[counter].append(e)
            if addition:
                counter += 1
            else: 
                counter -= 1
            if counter == numRows-1:
                addition = False
            elif counter == 0:
                addition = True
        
        strin = ''
        for smol in thicc_container:
            strin = strin + ''.join(smol)
        return strin