class Solution:
    def findRotateSteps(self, ring, key):
        n = len(ring)
        m = len(key)
        
        # Map each character to all positions it appears at in ring
        from collections import defaultdict
        char_positions = defaultdict(list)
        for i, c in enumerate(ring):
            char_positions[c].append(i)
        
        # dp[pos] = min steps to spell key so far, ending with ring's pos at 12:00
        dp = {0: 0}  # initially ring[0] is at 12:00, 0 steps taken
        
        for ch in key:
            new_dp = {}
            for pos in char_positions[ch]:
                best = float('inf')
                for prev_pos, steps in dp.items():
                    # distance to rotate from prev_pos to pos (clockwise or anticlockwise)
                    diff = abs(pos - prev_pos)
                    dist = min(diff, n - diff)
                    total = steps + dist + 1  # +1 for pressing the button
                    best = min(best, total)
                new_dp[pos] = best
            dp = new_dp
        
        return min(dp.values())