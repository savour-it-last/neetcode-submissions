# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _dfs_path_sums(self, node: Optional[TreeNode]) -> int:
        """
        Finds max sums of paths
        """
        if not node:
            return 0

        left = self._dfs_path_sums(node.left)
        right = self._dfs_path_sums(node.right)

        # best complete path through node
        current_max = node.val + left + right 

        # update global max
        if current_max > self.max_sum:
            self.max_sum = current_max

        # return upward contribution
        child_contribution = max(left, right)
        contribution =  node.val + (child_contribution if child_contribution > 0 else 0)
        return contribution if contribution > 0 else 0
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        self._dfs_path_sums(node=root)
        return int(self.max_sum)
        