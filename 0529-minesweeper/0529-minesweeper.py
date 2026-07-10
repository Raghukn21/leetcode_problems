class Solution:
    def updateBoard(self, board, click):
        row, col = click
        
        # Rule 1: clicked on a mine
        if board[row][col] == 'M':
            board[row][col] = 'X'
            return board
        
        rows, cols = len(board), len(board[0])
        
        def get_neighbors(r, c):
            neighbors = []
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        neighbors.append((nr, nc))
            return neighbors
        
        def dfs(r, c):
            if board[r][c] != 'E':
                return
            
            neighbors = get_neighbors(r, c)
            mine_count = sum(1 for nr, nc in neighbors if board[nr][nc] == 'M')
            
            if mine_count > 0:
                board[r][c] = str(mine_count)
            else:
                board[r][c] = 'B'
                for nr, nc in neighbors:
                    dfs(nr, nc)
        
        dfs(row, col)
        return board