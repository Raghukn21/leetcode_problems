from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        result = 0

        for i in range(len(points)):
            dist_count = defaultdict(int)

            for j in range(len(points)):
                if i == j:
                    continue
                # Use squared distance to avoid floating-point issues with sqrt
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dist_sq = dx * dx + dy * dy
                dist_count[dist_sq] += 1

            # For each group of k points equidistant from i:
            # ordered pairs (j, k) where j != k = k * (k-1)
            for count in dist_count.values():
                result += count * (count - 1)

        return result