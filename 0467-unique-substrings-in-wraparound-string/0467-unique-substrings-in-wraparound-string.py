class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # max_len[c] = length of the longest consecutive substring of s
        # that is valid (exists in base) and ends with character c
        max_len = {}
        current_len = 0

        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1])) % 26 == 1:
                current_len += 1  # extends the previous consecutive run
            else:
                current_len = 1   # starts a new run of length 1

            # For this ending character, keep the longest run we've ever seen
            max_len[ch] = max(max_len.get(ch, 0), current_len)

        return sum(max_len.values())