class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        word_set = set(words)
        result = []

        def can_form(word):
            """
            Returns True if 'word' can be split into 2+ words from word_set,
            where each component is strictly shorter than 'word' itself.
            Uses a standard word-break DP.
            """
            n = len(word)
            if n == 0:
                return False

            # dp[i] = True if word[0:i] can be formed by words from word_set
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    segment = word[j:i]
                   
                    if dp[j] and len(segment) < n and segment in word_set:
                        dp[i] = True
                        break  # no need to try other j values for this i

            return dp[n]

        for word in words:
            if can_form(word):
                result.append(word)

        return result