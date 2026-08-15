class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posD = set()
        negD = set()
        sols = []
        board = [["."] * n for i in range(n)]
        def backtrack(row):
            if row == n:
                copy = ["".join(row) for row in board]
                sols.append(copy)
                return
            for col in range(n):
                if col in cols or (col-row) in negD or (col + row) in posD:
                    continue
                cols.add(col)
                negD.add(col-row)
                posD.add(col + row)

                board[col][row] = "Q" 
                backtrack(row + 1)
                board[col][row] = "."

                cols.remove(col)
                negD.remove(col-row)
                posD.remove(col + row)
        backtrack(0)
        return sols




        