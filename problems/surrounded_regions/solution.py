class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        notsur = []
        for row in range(len(board)):
            for column in range(len(board[0])):
                if row == 0 or row == len(board)-1 or column == 0 or column == len(board[0])-1:
                    if board[row][column] =="O":
                        dfs = deque([[row,column]])
                        while dfs:
                            cord = dfs.pop()
                            locrow = cord [0]
                            loccol = cord [1]
                            node = board [locrow] [loccol]
                            if node == "O":
                                notsur.append([locrow,loccol])
                                board [locrow][loccol] = "X"


                            if locrow < len(board)-1 :
                                if board [locrow+1][loccol] =="O":
                                    dfs.append([locrow+1,loccol])
                            if locrow > 0 :
                                if board [locrow-1][loccol] =="O" :
                                    dfs.append([locrow-1,loccol])
                            if loccol < len(board[row])-1 :
                                if board [locrow][loccol+1] =="O":
                                    dfs.append([locrow,loccol+1])
                            if loccol > 0 :
                                if board [locrow][loccol-1] =="O":
                                    dfs.append([locrow,loccol-1])
        for row in range(len(board)):
            for column in range(len(board[0])):
                board[row][column]= "X"
        for el in notsur:
            board[el[0]][el[1]] = "O"
        