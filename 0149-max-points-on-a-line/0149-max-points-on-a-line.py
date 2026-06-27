from math import gcd
from collections import defaultdict

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n  # any 1 or 2 points are trivially "on the same line"

        max_count = 1

        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]

            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1

                # Normalize the slope to a canonical reduced form
                if dx == 0:
                    slope = ('inf', 0)  # vertical line
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g
                    # Ensure a consistent sign convention (e.g., dx always positive)
                    # so that (dy, dx) and (-dy, -dx) are treated as the same slope
                    if dx < 0:
                        dx, dy = -dx, -dy
                    slope = (dy, dx)

                slopes[slope] += 1
                max_count = max(max_count, slopes[slope] + 1)  # +1 to include the anchor point itself

        return max_count