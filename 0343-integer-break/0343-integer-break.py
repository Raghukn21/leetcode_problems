class Solution:
    def integerBreak(self, n: int) -> int:
        # Small cases handled directly, since the "break into 3s" rule
        # needs at least one full group of 3 to make sense
        if n == 2:
            return 1  # 1*1
        if n == 3:
            return 2  # 1*2

        product = 1
        while n > 4:
            product *= 3
            n -= 3
        product *= n  # multiply in whatever's left: 2, 3, or 4

        return product