class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        count = 0
        m, n = len(board), len(board[0])

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'X':
                    # Only count this cell if it's the TOP-LEFT start of a battleship:
                    # no 'X' above it (would mean it's part of a vertical ship started earlier)
                    # no 'X' to the left (would mean it's part of a horizontal ship started earlier)
                    if (r == 0 or board[r - 1][c] != 'X') and \
                       (c == 0 or board[r][c - 1] != 'X'):
                        count += 1

        return count