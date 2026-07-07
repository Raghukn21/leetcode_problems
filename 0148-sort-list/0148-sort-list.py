class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into two halves using slow/fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None  # cut the list into two halves
        
        # Step 2: Recursively sort each half
        left = self.sortList(head)
        right = self.sortList(second)
        
        # Step 3: Merge the two sorted halves
        return self._merge(left, right)
    
    def _merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 if l1 else l2
        
        return dummy.next