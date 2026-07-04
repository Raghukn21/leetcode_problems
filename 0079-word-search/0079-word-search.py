class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True  # matched all characters — found the word

            if r < 0 or r >= m or c < 0 or c >= n:
                return False  # out of bounds

            if board[r][c] != word[idx]:
                return False  # character mismatch

            if board[r][c] == '#':
                return False  # already visited on this path

            # Mark this cell as visited for the current path
            temp = board[r][c]
            board[r][c] = '#'

            # Explore all 4 neighbors for the next character
            found = (
                dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1)
            )

            # Restore the cell (backtrack)
            board[r][c] = temp

            return found

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True

        return False