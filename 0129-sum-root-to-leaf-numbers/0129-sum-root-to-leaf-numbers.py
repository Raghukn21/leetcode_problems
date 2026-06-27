class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, current_number):
            if node is None:
                return 0

            current_number = current_number * 10 + node.val

            # Leaf node: this path is complete, return the number it represents
            if node.left is None and node.right is None:
                return current_number

            # Otherwise, continue down both children and sum their contributions
            return dfs(node.left, current_number) + dfs(node.right, current_number)

        return dfs(root, 0)