class Solution:
    def countArrangement(self, n):
        used = [False] * (n + 1)
        
        def backtrack(pos):
            if pos > n:
                return 1
            
            count = 0
            for num in range(1, n + 1):
                if not used[num] and (num % pos == 0 or pos % num == 0):
                    used[num] = True
                    count += backtrack(pos + 1)
                    used[num] = False
            
            return count
        
        return backtrack(1)