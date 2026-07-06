class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def mark_safe(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'  # Mark as safe
            # Check all four neighbors
            mark_safe(r + 1, c)
            mark_safe(r - 1, c)
            mark_safe(r, c + 1)
            mark_safe(r, c - 1)
            
        # 1. Mark 'O's connected to boundaries
        for r in range(rows):
            mark_safe(r, 0)
            mark_safe(r, cols - 1)
        for c in range(cols):
            mark_safe(0, c)
            mark_safe(rows - 1, c)
            
        # 2 & 3. Capture surrounded 'O's and restore safe 'T's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'