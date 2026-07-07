class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1
        
        s = [1, 2, 2]
        head = 2
        next_num = 1
        count = 1  # There is one '1' in the initial [1, 2, 2]
        
        while len(s) < n:
            times = s[head]
            for _ in range(times):
                s.append(next_num)
                if next_num == 1 and len(s) <= n:
                    count += 1
            next_num = 3 - next_num  # Toggle between 1 and 2
            head += 1
            
        return count