class Solution:
    def invert_node_children(self, root: TreeNode) -> TreeNode:
        """
        Swap the left and right children of a node
        """
        tmp = root.left
        root.left = root.right
        root.right = tmp
        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Preserve original references BEFORE any mutation
        original_left = root.left
        original_right = root.right

        # 1. Recurse on original left
        self.invertTree(original_left)

        # 2. Process current node (inorder "middle")
        self.invert_node_children(root)

        # 3. Recurse on original right
        self.invertTree(original_right)

        return root