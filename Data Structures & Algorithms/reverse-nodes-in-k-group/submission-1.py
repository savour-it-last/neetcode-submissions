# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def _reverse_k_nodes(self, head: ListNode, k: int) -> tuple[ListNode| None, ListNode | None]:
        """
        Ts returns the start of the next sequence or None and current tail.
        """
        old_head = head
        curr = head
        next_ = head.next
        counter = k
        for i in range(k):
            if not head:
                # so next head would be None, and curr would be as is.
                return head, curr
            head = head.next
        for i in range(k-1):
            tmp = next_.next
            next_.next = curr
            curr = next_
            next_ = tmp
            k-=1
        old_head.next = next_
        return next_, curr
            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Do a local reversal, should be easy
        # trick is current reversed list should point to next
        # recurring pattern is current head, point to next tail.
        # I can just make the above function return the tail. And then have the new head of next in line connect.
        prev_tail = None
        while head:
            next_head, curr_head= self._reverse_k_nodes(head=head, k=k)
            #connects previous ordering to current
            if prev_tail:
                prev_tail.next = curr_head
            else:
                # if there is no previous head, we found the lists
                # new head
                new_head = curr_head
            prev_tail = head
            head = next_head
        return new_head
