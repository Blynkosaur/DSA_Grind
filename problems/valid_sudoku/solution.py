class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares =  [[[],[],[]],
                    [[],[],[]],
                    [[],[],[]]]
        square_counter = [0,0]
        rows = [[],[],[],[],[],[],[],[],[]]
        
        columns = [[],[],[],[],[],[],[],[],[]]
        
        for row in range(9):
            for column in range(9):
                if board[row][column] != ".":
                    if board[row][column] not in rows[row]:
                        rows[row].append(board[row][column])
                    else:
                        print(row)
                        return False
                    if board[row][column] not in columns[column]:
                        columns[column].append(board[row][column])
                    else:
                        print(columns)
                        return False
                    square_counter[0] = int(row/3)
                    square_counter[1] = int(column/3)
                    if board[row][column] not in squares[square_counter[0]][square_counter[1]]:
                        squares[square_counter[0]][square_counter[1]].append(board[row][column])
                    else:
                        print(squares)
                        return False
        
        return True

                    

