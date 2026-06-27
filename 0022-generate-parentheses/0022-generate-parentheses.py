class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, open_count, close_count):
            # Base case: used all n pairs
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            # We can add '(' as long as we haven't used all n yet
            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()

            # We can add ')' only if it won't exceed the number of '(' already placed
            if close_count < open_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()

        backtrack([], 0, 0)
        return result