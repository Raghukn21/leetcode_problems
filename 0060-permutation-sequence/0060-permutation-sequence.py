from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(i) for i in range(1, n + 1)]
        result = []
        k -= 1  # convert to 0-indexed, since "1st permutation" should map to index 0

        for i in range(n, 0, -1):
            fact = factorial(i - 1)  # number of permutations possible with remaining digits
            index = k // fact        # which digit (from what's left) goes in this position
            result.append(digits[index])
            digits.pop(index)        # remove the used digit so it can't be picked again
            k %= fact                 # narrow down k to the position within the remaining block

        return "".join(result)