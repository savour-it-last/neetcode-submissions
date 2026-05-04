# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def compare_subtree(self, p: TreeNode, q: TreeNode) -> bool:
        if (
            p.val == q.val
            and ((p.left is None and q.left is None) or (p.left.val == q.left.val))
            and ((p.right is None and q.right is None) or (p.right.val == q.right.val))
        ):
            return True
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False
        if not self.isSameTree(p = p.left, q = q.left):
            return False
        if not self.isSameTree(p=p.right, q = q.right):
            return False
        return True
