class Solution:
    def checkSubarraySum(self, nums, k):
        remainder_map = {0: -1}  # remainder -> earliest index seen
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i
        
        return False