class Solution:
    def findPairs(self, nums, k):
        from collections import Counter
        
        count = Counter(nums)
        result = 0
        
        if k == 0:
            # Count numbers that appear at least twice
            for num, freq in count.items():
                if freq >= 2:
                    result += 1
        else:
            # Count numbers where num + k also exists
            for num in count:
                if num + k in count:
                    result += 1
        
        return result