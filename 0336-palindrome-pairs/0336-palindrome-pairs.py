class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        word_to_index = {word: i for i, word in enumerate(words)}
        result = []

        def is_palindrome(s):
            return s == s[::-1]

        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):  # split points: 0 to n (inclusive, to handle empty prefix/suffix)
                prefix = word[:j]
                suffix = word[j:]

                # Case A: if prefix is a palindrome, we need a word equal to
                # reverse(suffix) to go BEFORE this word:
                # reverse(suffix) + word = reverse(suffix) + prefix + suffix
                # Since prefix is a palindrome, this reduces to checking
                # reverse(suffix) + palindrome + suffix, which is a palindrome
                # overall if reverse(suffix) and suffix are reverses of each other
                # (which they are by construction) — so we just need that word to exist.
                if is_palindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_to_index:
                        k = word_to_index[reversed_suffix]
                        if k != i:
                            result.append([k, i])

                # Case B: if suffix is a palindrome, we need a word equal to
                # reverse(prefix) to go AFTER this word.
                # Avoid double-counting the case j == n (empty suffix), since
                # that's already covered by Case A with j=0 for the same pair.
                if j != n and is_palindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_to_index:
                        k = word_to_index[reversed_prefix]
                        if k != i:
                            result.append([i, k])

        return result