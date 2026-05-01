# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_linked_list(self, head: Optional(ListNode)) -> Optional(ListNode):
        """
        reverse linked list and return new head
        """
        prev = None
        while head:
            tmp = head.next
            head.next =  prev
            prev = head
            head = tmp
        return prev

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        reverse_head = self.reverse_linked_list(head=head)
        count = 1
        current_head = reverse_head
        prev = None
        while reverse_head:
            if count == n:
                if not prev:
                    tmp = reverse_head.next
                    reverse_head.next = None
                    reverse_head = tmp
                    current_head = reverse_head
                else:
                    prev.next = reverse_head.next
                    reverse_head = reverse_head.next
            else:
                prev = reverse_head
                reverse_head = reverse_head.next
            
            count+=1
        if not prev:
            return None

        original_head = self.reverse_linked_list(head=current_head)
        return original_head

