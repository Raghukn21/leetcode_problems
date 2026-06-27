class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        n = len(s)

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start, current_partition):
            # Base case: we've reached the end of the string,
            # meaning current_partition is a complete valid partitioning
            if start == n:
                result.append(current_partition[:])
                return

            for end in range(start, n):
                if is_palindrome(start, end):
                    current_partition.append(s[start:end + 1])
                    backtrack(end + 1, current_partition)
                    current_partition.pop()  # backtrack: undo this choice

        backtrack(0, [])
        return result