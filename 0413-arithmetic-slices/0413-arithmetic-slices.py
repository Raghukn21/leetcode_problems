class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        # dp[i] stores the number of arithmetic subarrays ending at index i
        dp = [0] * n
        total_count = 0
        
        for i in range(2, n):
            # Check if the last three elements form an arithmetic sequence
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
                total_count += dp[i]
                
        return total_count