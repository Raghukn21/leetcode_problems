class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # is_pal[i][j] = True if s[i:j+1] is a palindrome
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n):
            is_pal[i][i] = True  # single characters are always palindromes

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or is_pal[i + 1][j - 1]:
                        is_pal[i][j] = True

        # min_cuts[i] = minimum cuts needed to partition s[0:i+1]
        min_cuts = [0] * n

        for i in range(n):
            if is_pal[0][i]:
                # The whole prefix s[0:i+1] is itself a palindrome — 0 cuts needed
                min_cuts[i] = 0
            else:
                min_cuts[i] = float('inf')
                for j in range(i):
                    # If s[j+1:i+1] is a palindrome, we can cut right after j,
                    # building on the best solution for s[0:j+1]
                    if is_pal[j + 1][i] and min_cuts[j] + 1 < min_cuts[i]:
                        min_cuts[i] = min_cuts[j] + 1

        return min_cuts[n - 1]