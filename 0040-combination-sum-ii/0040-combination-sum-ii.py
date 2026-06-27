class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []

        def backtrack(start, remaining, current):
            if remaining == 0:
                result.append(current[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                # (but allow reuse across different branches/depths)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since sorted, if even the smallest remaining candidate
                # exceeds what's left, no further candidate can work either
                if candidates[i] > remaining:
                    break

                current.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], current)
                current.pop()

        backtrack(0, target, [])
        return result