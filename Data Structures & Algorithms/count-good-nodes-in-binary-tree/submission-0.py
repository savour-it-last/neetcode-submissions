# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, node: TreeNode|None, curr_max: int) -> int:
        if not node:
            return 0
        count = 0
        if curr_max <= node.val:
            count+=1
        curr_max = max(curr_max, node.val)
        count+= self.check(node=node.left, curr_max=curr_max)
        count+= self.check(node=node.right, curr_max=curr_max)
        return count


        
    def goodNodes(self, root: TreeNode) -> int:
        return self.check(node=root, curr_max=root.val)

        