class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n  # everyone starts with at least 1 candy

        # Left-to-right pass: if this child's rating is higher than the
        # previous child's, they must get more candy than that neighbor.
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right-to-left pass: if this child's rating is higher than the
        # next child's, they must get more candy than that neighbor too.
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)