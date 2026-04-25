# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        curr_ = head
        next_ = curr_.next
        prev_: Optional[ListNode] = None
        while curr_:
            curr_.next = prev_
            prev_ = curr_
            curr_ = next_
            next_ = curr_.next if curr_ else None
        return prev_
            
                


        
        return tail
        
        
        