class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # If the start or end is blocked, there are no valid paths at all
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        # First column: each cell is reachable only from the cell above —
        # but if any cell in the column is an obstacle, every cell below it
        # is also unreachable (since the robot can only move right or down,
        # the only path down the first column is completely blocked by any obstacle)
        for r in range(1, m):
            dp[r][0] = 0 if obstacleGrid[r][0] == 1 else dp[r - 1][0]

        # First row: same reasoning — any obstacle blocks all cells to its right
        for c in range(1, n):
            dp[0][c] = 0 if obstacleGrid[0][c] == 1 else dp[0][c - 1]

        # Fill the rest: obstacles get 0, others sum from above and left
        for r in range(1, m):
            for c in range(1, n):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[m - 1][n - 1]