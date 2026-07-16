"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # hash that stores original node and what it point to.
        # original and what it is in curr
        random_hash = {}
        org_head = head
        prev = Node(0)
        dummy = prev
        while org_head:
            curr = Node(x = org_head.val, next=None, random=org_head.random)
            prev.next = curr
            random_hash[org_head] = curr
            prev = curr
            org_head = org_head.next
        
        curr = dummy.next
        while curr:
            if curr.random:
                curr.random = random_hash[curr.random]
            curr = curr.next
        
        return dummy.next
        
        
        