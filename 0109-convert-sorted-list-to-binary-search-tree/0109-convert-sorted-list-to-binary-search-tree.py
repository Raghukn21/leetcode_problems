# Definition for a singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Step 1: Count the number of nodes
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
            
        self.head = head
        
        # Step 2: Build the tree using in-order traversal simulation
        def convert(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            # Build left subtree
            left_child = convert(left, mid - 1)
            
            # Build current node
            node = TreeNode(self.head.val)
            node.left = left_child
            self.head = self.head.next
            
            # Build right subtree
            node.right = convert(mid + 1, right)
            
            return node
            
        return convert(0, size - 1)