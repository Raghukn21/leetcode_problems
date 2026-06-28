class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        jumps = 0
        current_end = 0    # farthest index reachable with the jumps used so far
        farthest = 0        # farthest index reachable with one more jump

        for i in range(n - 1):  # no need to consider the last index as a jump-from point
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps