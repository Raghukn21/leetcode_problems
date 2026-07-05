# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        while True:
            # Combine two rand7() calls to get a uniform value in [1, 49]
            # Think of it as: row in [0,6], col in [0,6], giving a 7x7 grid
            row = rand7() - 1   # 0 to 6
            col = rand7() - 1   # 0 to 6
            idx = row * 7 + col  # 0 to 48 (uniform across all 49 values)

            if idx < 40:         # keep only [0, 39] — exactly 40 values
                return idx % 10 + 1  # map evenly to [1, 10]
            # else: discard and retry (rejection sampling)