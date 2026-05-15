# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_val = preorder.pop(0)
        root = TreeNode(val = root_val)
        inorder_root_index = inorder.index(root_val)
        left_inorder = inorder[:inorder_root_index]
        left_subtree_size = len(left_inorder)
        right_inorder = inorder[inorder_root_index+1:]
        left_preorder = preorder[:left_subtree_size]
        right_preorder = preorder[left_subtree_size:]
        left_subtree_root = self.buildTree(preorder=left_preorder, inorder=left_inorder)
        right_subtree_root = self.buildTree(preorder=right_preorder, inorder=right_inorder)
        root.left = left_subtree_root
        root.right = right_subtree_root
        return root
