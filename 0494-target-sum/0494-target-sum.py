class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        
        
        if total_sum < abs(target) or (target + total_sum) % 2 != 0:
            return 0
            
        p = (target + total_sum) // 2
        
        
        dp = [0] * (p + 1)
        dp[0] = 1  
        
        for num in nums:
            for j in range(p, num - 1, -1):
                dp[j] += dp[j - num]
                
        return dp[p]