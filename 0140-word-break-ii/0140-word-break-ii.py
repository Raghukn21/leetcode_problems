class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        n = len(s)
        memo = {}  # start_index -> list of all valid sentences for s[start_index:]

        def backtrack(start):
            if start == n:
                return [""]  # base case: empty suffix has exactly one "sentence" — the empty one

            if start in memo:
                return memo[start]

            sentences = []
            for end in range(start + 1, n + 1):
                word = s[start:end]
                if word in word_set:
                    # Recursively get all valid sentences for the rest of the string
                    rest_sentences = backtrack(end)
                    for rest in rest_sentences:
                        if rest == "":
                            sentences.append(word)
                        else:
                            sentences.append(word + " " + rest)

            memo[start] = sentences
            return sentences

        return backtrack(0)