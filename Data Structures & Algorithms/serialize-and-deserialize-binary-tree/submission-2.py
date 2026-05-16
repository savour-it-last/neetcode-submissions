# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        tree_list = []
        tree_queue = []
        tree_queue = deque([root])
        while tree_queue:
            node = tree_queue.popleft()
            tree_list.append(str(node.val) if node else "None")
            if node:
                tree_queue.append(node.left)
                tree_queue.append(node.right)
        return ",".join(tree_list)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        tree_list = deque(data.split(","))
        root_val = tree_list.popleft()
        root = TreeNode(val=int(root_val))
        tree_roots_queue = deque([root])
        while tree_list or tree_roots_queue:
            node = tree_roots_queue.popleft()
            if not node:
                continue
            left_val = tree_list.popleft()
            right_val = tree_list.popleft()
            left = TreeNode(val = int(left_val)) if left_val != "None" else None
            right = TreeNode(val = int(right_val)) if right_val != "None" else None
            node.left = left
            node.right = right
            if left:
                tree_roots_queue.append(left)
            if right:
                tree_roots_queue.append(right)
        return root
        

            

            

        
