import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie
        if rounds == 0:
            return 0

        pigs = 0
        while (rounds + 1) ** pigs < buckets:
            pigs += 1
        return pigs