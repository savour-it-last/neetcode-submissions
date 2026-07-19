# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def calc_max_length(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        # calculate length if pivoting
        left_height = self.calc_max_length(root=root.left)
        right_height = self.calc_max_length(root=root.right)
        pivoting_length = left_height + right_height
        non_pivoting_length = 1 + max(
            left_height,
            right_height,
        )
        self.max_length = max(pivoting_length, self.max_length)
        return non_pivoting_length


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # algo is max height till that node.
        # The decision I guess is including the current node or not.
        # If including, curr length + 1
        # Otherwise we reset to 0.
        # First is pivot where we take current node as center
        # and see if longest passes through int
        # second is we take max of left or right
        self.max_length = 0
        self.calc_max_length(root=root)
        return self.max_length
