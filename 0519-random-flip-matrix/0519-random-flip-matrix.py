import random

class Solution:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.total = m * n
        self.remaining = self.total
        self.mapping = {}  # maps a "swapped" index to its replacement value

    def flip(self):
        # Pick a random index among the remaining unflipped cells
        rand_idx = random.randrange(self.remaining)
        
        # Find what value this index actually maps to (if it was swapped before)
        result = self.mapping.get(rand_idx, rand_idx)
        
        # Move the last remaining index into this slot
        last_idx = self.remaining - 1
        self.mapping[rand_idx] = self.mapping.get(last_idx, last_idx)
        
        # Shrink the pool of remaining indices
        self.remaining -= 1
        
        # Convert flat index to (row, col)
        return [result // self.n, result % self.n]

    def reset(self):
        self.remaining = self.total
        self.mapping = {}