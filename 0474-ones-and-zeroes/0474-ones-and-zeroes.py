class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        # dp[i][j] will store the max subset size with i zeros and j ones
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for s in strs:
            zeros = s.count('0')
            ones = len(s) - zeros
            
            # Traverse backwards to prevent using the same string multiple times
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])
                    
        return dp[m][n]