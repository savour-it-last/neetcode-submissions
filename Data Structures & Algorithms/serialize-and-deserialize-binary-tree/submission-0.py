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
        tree_queue.append(root)
        while tree_queue:
            node = tree_queue.pop(0)
            tree_list.append(str(node.val) if node else "None")
            if node:
                tree_queue.extend([node.left, node.right])
        return ",".join(tree_list)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        tree_list = data.split(",")
        root_val = tree_list.pop(0)
        root = TreeNode(val=int(root_val))
        tree_roots_stack = []
        tree_roots_stack.append(root)
        while tree_list or tree_roots_stack:
            node = tree_roots_stack.pop(0)
            if not node:
                continue
            left_val = tree_list.pop(0)
            right_val = tree_list.pop(0)
            left = TreeNode(val = int(left_val)) if left_val != "None" else None
            right = TreeNode(val = int(right_val)) if right_val != "None" else None
            node.left = left
            node.right = right
            tree_roots_stack.extend([left,right])
        return root
        

            

            

        
