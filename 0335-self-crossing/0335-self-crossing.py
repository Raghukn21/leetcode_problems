class Solution:
    def isSelfCrossing(self, distance: list[int]) -> bool:
        d = distance
        n = len(d)

        for i in range(3, n):
            # Case 1: current line crosses the line 3 steps before it
            # (the 4th-most-recent move "boxes in" and overlaps the current one)
            if d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]:
                return True

            # Case 2: current line crosses the line 4 steps before it
            # (a tight spiral where the 5th-most-recent segment gets clipped)
            if i >= 4:
                if (d[i - 1] == d[i - 3] and
                        d[i] + d[i - 4] >= d[i - 2]):
                    return True

            # Case 3: current line crosses the line 5 steps before it
            # (a looser spiral that still wraps back onto an earlier segment)
            if i >= 5:
                if (d[i - 2] >= d[i - 4] and
                        d[i] + d[i - 4] >= d[i - 2] and
                        d[i - 1] + d[i - 5] >= d[i - 3] and
                        d[i - 1] <= d[i - 3]):
                    return True

        return False