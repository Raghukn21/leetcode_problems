import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.nums = []
        self.idx_map = defaultdict(set)

    def insert(self, val: int) -> bool:
        # Check if the value exists
        exists = val in self.idx_map
        
        # Add index to the map and value to the list
        self.idx_map[val].add(len(self.nums))
        self.nums.append(val)
        
        return not exists

    def remove(self, val: int) -> bool:
        if val not in self.idx_map or not self.idx_map[val]:
            return False
        
        # Get an index of the element to remove
        idx_to_remove = self.idx_map[val].pop()
        last_val = self.nums[-1]
        
        # Swap with the last element
        self.nums[idx_to_remove] = last_val
        self.idx_map[last_val].add(idx_to_remove)
        self.idx_map[last_val].remove(len(self.nums) - 1)
        
        # Pop the last element
        self.nums.pop()
        
        # Cleanup map if set is empty
        if not self.idx_map[val]:
            del self.idx_map[val]
            
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)