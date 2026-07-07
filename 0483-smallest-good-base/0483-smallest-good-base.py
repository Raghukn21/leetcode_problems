class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        # Max possible length m is log2(num) + 1
        max_m = num.bit_length()
        
        # Try decreasing values of m (number of 1s) from max_m down to 3
        for m in range(max_m, 2, -1):
            # Estimate k using m-1 power root of num
            k = int(num ** (1 / (m - 1)))
            if k < 2:
                continue
                
            # Verify if this k satisfies (k^m - 1) / (k - 1) == num
            # Sum of geometric progression: sum_{i=0}^{m-1} k^i
            current_sum = 0
            p = 1
            for _ in range(m):
                current_sum += p
                p *= k
                
            if current_sum == num:
                return str(k)
                
        # If no m >= 3 works, base is num - 1 (since num = 11 in base num-1)
        return str(num - 1)