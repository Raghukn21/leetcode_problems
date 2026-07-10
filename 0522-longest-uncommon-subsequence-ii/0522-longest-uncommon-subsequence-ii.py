class Solution:
    def findLUSlength(self, strs):
        def is_subsequence(a, b):
            # checks if a is a subsequence of b
            it = iter(b)
            return all(c in it for c in a)
        
        result = -1
        
        for i in range(len(strs)):
            is_uncommon = True
            for j in range(len(strs)):
                if i != j and is_subsequence(strs[i], strs[j]):
                    is_uncommon = False
                    break
            if is_uncommon:
                result = max(result, len(strs[i]))
        
        return result