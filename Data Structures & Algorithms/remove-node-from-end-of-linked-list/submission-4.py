# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(val=0, next=head)
        left = dummy
        count = 0
        while count!=n and head:
            head = head.next
            count+=1
        right = head
        while right and left:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next