class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        vert_d = set()
        neg_d = set()
        total = 0
        def backtrack(row):
            nonlocal total
            if row == n:
                total += 1
                return
            for col in range(n):
                if col not in cols and (col - row) not in neg_d and col + row not in vert_d:
                    cols.add(col)
                    neg_d.add(col-row)
                    vert_d.add(col+row)

                    backtrack(row + 1)

                    cols.remove(col)
                    neg_d.remove(col-row)
                    vert_d.remove(col+row)
        backtrack(0)
        return total


            

        