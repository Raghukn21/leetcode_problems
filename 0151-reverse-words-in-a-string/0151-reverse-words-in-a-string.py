class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()  # splits on any whitespace, ignoring leading/trailing/multiple spaces
        words.reverse()
        return " ".join(words)