class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(start: int, path: list[int]):
            if len(path) >= 2:
                res.append(list(path))
                
            used = set()
            for i in range(start, len(nums)):
                
                if nums[i] in used:
                    continue
               
                if path and nums[i] < path[-1]:
                    continue
                    
                used.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                
        backtrack(0, [])
        return res