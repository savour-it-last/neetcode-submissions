# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        result = []
        queue.append(root)
        while queue:
            qLength = len(queue)
            level_list = []
            for i in range(qLength):
                node = queue.popleft()
                if node:
                    level_list.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level_list:
                result.append(level_list)
        return result

