# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = 1
        left_count = self.maxDepth(root=root.left)
        right_count = self.maxDepth(root = root.right)
        count += max(left_count, right_count)
        return count
