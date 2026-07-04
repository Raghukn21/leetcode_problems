class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        def backtrack(start, current):
            if len(current) == k:
                result.append(current[:])
                return

            # Pruning: we need (k - len(current)) more numbers,
            # and they must all come from [start, n].
            # So start can go no higher than n - (k - len(current)) + 1,
            # otherwise there aren't enough numbers left to complete the combination.
            need = k - len(current)
            for num in range(start, n - need + 2):
                current.append(num)
                backtrack(num + 1, current)
                current.pop()

        backtrack(1, [])
        return result