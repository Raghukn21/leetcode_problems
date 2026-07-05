# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        dummy = ListNode(0, head)
        prev = dummy
        
        while head:
            # If next node exists and has same value, it's a duplicate
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Point prev.next to the node after the duplicates
                prev.next = head.next
            else:
                # No duplicate, move the prev pointer forward
                prev = prev.next
            
            # Move the head pointer forward
            head = head.next
            
        return dummy.next