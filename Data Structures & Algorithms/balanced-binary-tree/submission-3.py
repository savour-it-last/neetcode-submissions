# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _get_max_depth(self, root: Optional[TreeNode])->int:
        if not root:
            return 0
        left_depth = self._get_max_depth(root=root.left)
        if left_depth == -1:
            return -1
        right_depth = self._get_max_depth(root=root.right)
        if right_depth == -1:
            return -1
        if abs(right_depth-left_depth) > 1:
            return -1
        return 1 + max(left_depth, right_depth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self._get_max_depth(root=root)!=-1
        