from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val_freq = {}          
        self.freq_to_keys = defaultdict(OrderedDict) 

    def _increment_freq(self, key):
        """Moves key from its current freq bucket to freq+1 bucket."""
        val, freq = self.key_to_val_freq[key]

       
        del self.freq_to_keys[freq][key]

       
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1

       
        new_freq = freq + 1
        self.key_to_val_freq[key] = [val, new_freq]
        self.freq_to_keys[new_freq][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self._increment_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
           
            self.key_to_val_freq[key][0] = value
            self._increment_freq(key)
        else:
            
            if len(self.key_to_val_freq) == self.capacity:
               
                evicted_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_val_freq[evicted_key]

            
            self.key_to_val_freq[key] = [value, 1]
            self.freq_to_keys[1][key] = None
            self.min_freq = 1  