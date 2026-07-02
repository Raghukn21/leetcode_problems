class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(max_sum):
            count = 1
            current_sum = 0
            for num in nums:
                current_sum += num
                if current_sum > max_sum:
                    count += 1
                    current_sum = num
                    if count > k:
                        return False
            return True

        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid  # Try smaller
            else:
                left = mid + 1 # Need larger capacity
        
        return left