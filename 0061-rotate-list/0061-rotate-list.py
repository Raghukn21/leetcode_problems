# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        
        # 1. Calculate length and find the tail
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
            
        # 2. Close the list into a ring
        old_tail.next = head
        
        # 3. Find the new tail: (n - k % n - 1)
        new_tail = head
        for _ in range(n - (k % n) - 1):
            new_tail = new_tail.next
            
        # 4. New head is next of new tail, then break the ring
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head