class Solution:
    def convertBST(self, root):
        self.running_sum = 0
        
        def reverse_inorder(node):
            if not node:
                return
            
            reverse_inorder(node.right)
            
            self.running_sum += node.val
            node.val = self.running_sum
            
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root