from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        
        dp = [defaultdict(int) for _ in range(n)]
        result = 0

        for i in range(1, n):
            for j in range(i):
                d = nums[i] - nums[j]

               
                prev_count = dp[j][d]

                dp[i][d] += prev_count + 1
                
                result += prev_count

        return result