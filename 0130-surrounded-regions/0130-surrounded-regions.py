class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            board[r][c] = '#'  # temporarily mark as "safe" (border-connected)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: From every border cell that is 'O', mark its entire connected
        # region as safe ('#'), since anything touching the border can't be captured.
        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)

        # Step 2: Any 'O' remaining was never reached from the border,
        # meaning it's part of a fully surrounded region — capture it.
        # Any '#' was safe — restore it back to 'O'.
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'