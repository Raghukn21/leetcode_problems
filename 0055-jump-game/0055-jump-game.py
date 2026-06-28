class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0
        n = len(nums)

        for i in range(n):
            # If we can't even reach this index, we're stuck — fail immediately
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

        return True