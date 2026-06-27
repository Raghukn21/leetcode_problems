class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        cols = set()           # columns currently occupied
        diag1 = set()          # "/" diagonals occupied, identified by (row - col)
        diag2 = set()          # "\" diagonals occupied, identified by (row + col)
        queens = [-1] * n      # queens[row] = column of the queen placed in that row

        def backtrack(row):
            if row == n:
                # Build the board from the queens placement and save it
                board = []
                for r in range(n):
                    row_str = ["."] * n
                    row_str[queens[r]] = "Q"
                    board.append("".join(row_str))
                result.append(board)
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue  # conflicts with an existing queen

                # Place the queen
                queens[row] = col
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # Remove the queen (backtrack)
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return result