# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: 'TreeNode') -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            
            # Update the number formed by the current path
            current_sum = current_sum * 10 + node.val
            
            # If it's a leaf, return the accumulated sum
            if not node.left and not node.right:
                return current_sum
            
            # Otherwise, continue recursion for children
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)