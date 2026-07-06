class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
            
        def backtrack(start: int, path: list[str]):
            # Base case: if we've reached the end of the string
            if start == len(s):
                res.append(list(path))
                return
            
            # Explore all possible substrings starting from 'start'
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    # Choose
                    path.append(substring)
                    # Explore
                    backtrack(end, path)
                    # Un-choose (backtrack)
                    path.pop()
                    
        backtrack(0, [])
        return res