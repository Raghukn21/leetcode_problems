class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return (0, 0)  # (rob_this, not_rob_this) — both 0 for an empty node

            left_rob, left_not_rob = dfs(node.left)
            right_rob, right_not_rob = dfs(node.right)

            # If we rob this node, we CANNOT rob its children —
            # so we must take each child's "not robbed" value.
            rob_this = node.val + left_not_rob + right_not_rob

            # If we don't rob this node, each child is free to be
            # robbed or not — we take whichever is better, independently.
            not_rob_this = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)

            return (rob_this, not_rob_this)

        return max(dfs(root))