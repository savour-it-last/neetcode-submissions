class Node:
    def __init__(self, value: int, next = None)->None:
        self.value = value
        self.next = next

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        # build linked list for O(1) space
        prev = Node(0)
        dummy = prev

        # create the target linked list
        for i in range(1, len(nums)):
            curr = Node(i)
            prev.next = curr
            prev = curr
        
        i = 0
        curr = dummy.next
        while i< len(nums) and curr:
            if nums[i]<curr.value:
                return nums[i]
            i+=1
            curr = curr.next
        return nums[i]