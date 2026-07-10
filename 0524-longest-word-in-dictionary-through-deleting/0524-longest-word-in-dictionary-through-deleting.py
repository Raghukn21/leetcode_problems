class Solution:
    def findLongestWord(self, s, dictionary):
        def is_subsequence(word, s):
            it = iter(s)
            return all(c in it for c in word)
        
        result = ""
        
        for word in dictionary:
            if is_subsequence(word, s):
                if len(word) > len(result) or (len(word) == len(result) and word < result):
                    result = word
        
        return result