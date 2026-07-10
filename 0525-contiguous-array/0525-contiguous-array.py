class Solution:
    def findMaxLength(self, nums):
        count_index = {0: -1}  # running count -> earliest index seen
        count = 0
        max_len = 0
        
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            
            if count in count_index:
                max_len = max(max_len, i - count_index[count])
            else:
                count_index[count] = i
        
        return max_len