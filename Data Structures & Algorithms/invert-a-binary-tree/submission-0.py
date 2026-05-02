# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert_node_children(self, root: TreeNode)->TreeNode:
        """
        Invert the children of a root node
        """
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root = self.invert_node_children(root=root)
        left = root.left
        right = root.right
        left = self.invertTree(root=left)
        right = self.invertTree(root=right)
        return root