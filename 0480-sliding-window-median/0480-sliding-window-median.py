from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums, k):
        window = SortedList(nums[:k])
        result = []
        
        def get_median():
            mid = k // 2
            if k % 2 == 1:
                return float(window[mid])
            else:
                return (window[mid - 1] + window[mid]) / 2.0
        
        result.append(get_median())
        
        for i in range(k, len(nums)):
            window.remove(nums[i - k])  # remove outgoing element
            window.add(nums[i])         # add incoming element
            result.append(get_median())
        
        return result