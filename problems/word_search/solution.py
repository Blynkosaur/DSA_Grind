class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(row, column, letter, position, visited):
    # Check if the end of the word is reached
            if position == len(word) - 1:
                if board[row][column] == word[-1]:
                    return True
                else:
                    return False

            # If not, continue the search
            position += 1
            nxtletter = word[position]
            visited.append((row, column))

            # Check all four directions
            if row > 0 and board[row - 1][column] == nxtletter and (row - 1, column) not in visited:
                if search(row - 1, column, nxtletter, position, visited):
                    return True
            if row < len(board) - 1 and board[row + 1][column] == nxtletter and (row + 1, column) not in visited:
                if search(row + 1, column, nxtletter, position, visited):
                    return True
            if column > 0 and board[row][column - 1] == nxtletter and (row, column - 1) not in visited:
                if search(row, column - 1, nxtletter, position, visited):
                    return True
            if column < len(board[0]) - 1 and board[row][column + 1] == nxtletter and (row, column + 1) not in visited:
                if search(row, column + 1, nxtletter, position, visited):
                    return True

            # If no valid paths are found, return False
            visited.pop()  # Backtrack
            return False


# Iterate over the board to find the starting point
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(i, j, word[0], 0, []):
                        return True
        return False

                