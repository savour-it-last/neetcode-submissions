# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def valid(self, node: Optional[TreeNode],left: int, right: int)->bool:
        if not node:
            return True
        if not (left<node.val<right):
            return False
        return self.valid(node = node.left, left = left, right = node.val) and self.valid(node = node.right, left = node.val, right = right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(node=root, left = float("-inf"), right = float("inf"))