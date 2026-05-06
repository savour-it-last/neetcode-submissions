# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = None
        flag = 0
        while root:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
            # elif (root.left.value <= p or root.left.value <= q) and (
            #     root.right.value >= p or root.right.value >= q
            # ):
            #     ancestor = root
            # elif root.value == p or root.value == q:
            #     flag+=1
            #     if not ancestor:
            #         ancestor = root




