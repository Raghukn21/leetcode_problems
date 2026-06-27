class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # prev tracks the node just before the pair we're about to swap
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            # Rewire the three pointers to swap 'first' and 'second'
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev forward by two nodes (past the now-swapped pair)
            prev = first

        return dummy.next