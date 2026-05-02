# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        # assume first value, it will get replaces
        ordered_list = dummy
        while not all(x is None for x in lists):
            min_index = 0
            for index in range(len(lists)):
                if not lists[index]:
                    continue
                if not lists[min_index] and lists[index]:
                    min_index = index
                    continue
                if lists[index].val < lists[min_index].val:
                    min_index = index
            ordered_list.next = lists[min_index]
            ordered_list = ordered_list.next
            lists[min_index] = lists[min_index].next
        return dummy.next

            



