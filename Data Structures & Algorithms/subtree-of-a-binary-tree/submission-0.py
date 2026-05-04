# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __check_subtree(self, target: TreeNode, subTree: TreeNode)->bool:
        """
        Check if subtree and target are same
        """
        if not target and not subTree:
            return True
        if (not target and subTree) or (not subTree and target):
            return False
        if target.val!=subTree.val:
            return False
        if not self.__check_subtree(target = target.left, subTree=subTree.left):
            return False
        if not self.__check_subtree(target= target.right, subTree= subTree.right):
            return False
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if root.val == subRoot.val and self.__check_subtree(target=root, subTree=subRoot):
            return True
        if self.isSubtree(root=root.left, subRoot=subRoot):
            return True
        if self.isSubtree(root=root.right, subRoot=subRoot):
            return True
        return False
