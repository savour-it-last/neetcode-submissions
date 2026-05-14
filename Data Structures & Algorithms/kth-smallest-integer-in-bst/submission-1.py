# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        stack.append(root)
        count = 0
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            count+=1
            curr = stack.pop(-1)
            if count == k:
                return curr.val
            curr = curr.right

            