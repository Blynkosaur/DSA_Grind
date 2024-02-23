class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        dummy = []
        hehe = [[]for x in range(n)]
        for i in range(n):
            for j in range(n):
                hehe[i].append(matrix[i][j])
        print(hehe)
        for i in range(n):
            dummy = []
            for j in range(n):
                dummy.append(hehe[j][i])
            dummy.reverse()
            print(dummy)
            print(hehe)
            matrix[i] = dummy
        
            
        