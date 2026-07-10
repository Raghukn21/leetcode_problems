class Solution:
    def findMinDifference(self, timePoints):
        minutes = []
        for t in timePoints:
            h, m = map(int, t.split(':'))
            minutes.append(h * 60 + m)
        
        minutes.sort()
        
        min_diff = float('inf')
        n = len(minutes)
        
        for i in range(1, n):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])
        
        # Check the circular wrap-around (last time to first time, going through midnight)
        wrap_diff = (minutes[0] + 1440) - minutes[-1]
        min_diff = min(min_diff, wrap_diff)
        
        return min_diff