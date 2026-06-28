class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []
        used = [False] * n

        def backtrack(current):
            if len(current) == n:
                result.append(current[:])
                return

            for i in range(n):
                if used[i]:
                    continue

                # Skip duplicates at the same recursion level:
                # if this value equals the previous one, and the previous
                # one hasn't been used (meaning we're choosing between
                # two "identical" branches), skip to avoid duplicate permutations
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False

        backtrack([])
        return result