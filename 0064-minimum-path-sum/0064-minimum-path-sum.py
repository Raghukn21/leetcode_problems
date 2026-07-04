class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]

        # First column: only reachable from above, so cumulative sum downward
        for r in range(1, m):
            dp[r][0] = dp[r - 1][0] + grid[r][0]

        # First row: only reachable from the left, so cumulative sum rightward
        for c in range(1, n):
            dp[0][c] = dp[0][c - 1] + grid[0][c]

        # Fill the rest: take the cheaper incoming direction + this cell's value
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]

        return dp[m - 1][n - 1]