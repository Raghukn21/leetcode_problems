class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        
        # Phase 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # fast reached the end -> no cycle
            return None
        
        # Phase 2: Find the start of the cycle
        ptr1 = head
        ptr2 = slow
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return ptr1