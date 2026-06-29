# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        result = []
        
        def dfs(node, remaining_sum, current_path):
            if not node:
                return
            
            # Add current node to the path
            current_path.append(node.val)
            
            # Check if it is a leaf node and the sum matches
            if not node.left and not node.right and node.val == remaining_sum:
                result.append(list(current_path))
            else:
                # Continue searching in children
                dfs(node.left, remaining_sum - node.val, current_path)
                dfs(node.right, remaining_sum - node.val, current_path)
            
            # Backtrack: remove current node before going back up
            current_path.pop()
            
        dfs(root, targetSum, [])
        return result