class Solution:
    def totalHammingDistance(self, nums: list[int]) -> int:
        total_distance = 0
        n = len(nums)
        
        # Iterate through each of the 32 bits
        for i in range(32):
            zeros = 0
            ones = 0
            
            # Check the i-th bit for every number in the array
            for num in nums:
                if (num >> i) & 1:
                    ones += 1
                else:
                    zeros += 1
            
            # Add the contribution of this bit position to the total
            total_distance += (zeros * ones)
            
        return total_distance