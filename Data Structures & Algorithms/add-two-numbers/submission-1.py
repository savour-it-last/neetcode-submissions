# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        curr = ListNode(0)
        dummy = curr
        while l1 or l2 or carry_over:
            curr.next = ListNode(0)
            curr = curr.next
            val = 0
            if not l1 and not l2:
                val = carry_over%10
                # since val takes unit place
                carry_over = carry_over//10
            elif l1 and not l2:
                # since val takes unit place
                val = (l1.val + carry_over)%10
                #carry over gonna be a value if you subtract val
                carry_over = ((l1.val + carry_over)//10)
                l1 = l1.next
            elif l2 and not l1:
                # since val takes unit place
                val = (l2.val + carry_over)%10
                #carry over gonna be a value if you subtract val
                carry_over = ((l2.val + carry_over)//10)
                l2 = l2.next
            elif l1 and l2:
                # since val takes unit place
                val = (l1.val + l2.val + carry_over)%10
                #carry over gonna be a value if you subtract val
                carry_over = ((l1.val + l2.val + carry_over)//10)
                l1 = l1.next
                l2 = l2.next
            curr.val = val
        return dummy.next