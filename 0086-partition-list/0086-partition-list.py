class Solution:
    def partition(self, head, x: int):
        # Dummy heads for the two partitions
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)

        less = less_dummy        # tail pointer for the "< x" partition
        greater = greater_dummy  # tail pointer for the ">= x" partition

        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next

        # Terminate the greater list (CRITICAL: avoids a cycle if the original
        # list's last node was in the "less" partition and still has a .next)
        greater.next = None

        # Join the two partitions
        less.next = greater_dummy.next

        return less_dummy.next