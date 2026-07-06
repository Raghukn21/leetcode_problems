class Solution:
    def grayCode(self, n: int) -> list[int]:
        # Generate the sequence using the bitwise formula
        return [i ^ (i >> 1) for i in range(1 << n)]