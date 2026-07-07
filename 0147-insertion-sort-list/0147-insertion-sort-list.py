class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        curr = head
        
        while curr:
            next_node = curr.next  # save next node to process later
            
            # Find insertion point in sorted list (starting from dummy)
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # Insert curr right after prev
            curr.next = prev.next
            prev.next = curr
            
            curr = next_node  # move to next node in original list
        
        return dummy.next