class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasc = {1:[1],2:[1,1]}
        answer = []
        def add(n):
            ls = pasc[n-1]
            back = []
            for i in range(len(ls)-1):
                back.append(ls[i]+ls[i+1])
            back.insert(0,1)
            back.insert(len(back),1)
            return back
        if numRows>2:
            for i in range(3,numRows+1):
                pasc[i] = add(i)
        for i in range(numRows):
            answer.append(pasc[i+1])
        return answer
        
        
        
