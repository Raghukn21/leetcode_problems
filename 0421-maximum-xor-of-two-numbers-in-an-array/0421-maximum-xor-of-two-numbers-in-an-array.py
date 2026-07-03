class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        L = len(bin(max(nums))) - 2
        trie = {}
        
        # Build the Trie
        for num in nums:
            node = trie
            for i in range(L, -1, -1):
                bit = (num >> i) & 1
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
        
        max_xor = 0
        # For each number, find the max XOR possible
        for num in nums:
            node = trie
            curr_xor = 0
            for i in range(L, -1, -1):
                bit = (num >> i) & 1
                toggled_bit = 1 - bit
                if toggled_bit in node:
                    curr_xor |= (1 << i)
                    node = node[toggled_bit]
                else:
                    node = node[bit]
            max_xor = max(max_xor, curr_xor)
            
        return max_xor