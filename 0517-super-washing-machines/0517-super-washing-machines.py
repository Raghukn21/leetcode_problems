class Solution:
    def findMinMoves(self, machines):
        n = len(machines)
        total = sum(machines)
        
        if total % n != 0:
            return -1
        
        avg = total // n
        max_moves = 0
        prefix_diff = 0
        
        for m in machines:
            diff = m - avg
            prefix_diff += diff
            # max of: current machine's own excess, or the flow needed across this boundary
            max_moves = max(max_moves, abs(prefix_diff), diff)
        
        return max_moves