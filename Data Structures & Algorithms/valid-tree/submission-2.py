class Solution:
    def check_circular_update_passed_nodes(
        self, parent: int, node: int, edges_dict: dict[int, set[int]]
    ) -> bool:
        """
        checks if when following a node either cycle or disconnectivity is present.
        """
        if node in self.visited:
            return False

        self.visited.add(node)

        for edge_end in edges_dict[node]:
            # going back to itself doesnt count as an issue
            if edge_end == parent:
                continue
            if not self.check_circular_update_passed_nodes(parent=node, node=edge_end, edges_dict=edges_dict):
                return False

        self.visited_all[node] = True
        return True

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edges_dict = {i: set() for i in range(n)}
        for edge in edges:
            edges_dict[edge[0]].add(edge[1])
            edges_dict[edge[1]].add(edge[0])

        self.visited_all = [False for i in range(n)]
        self.visited = set()
        if not self.check_circular_update_passed_nodes(parent=-1, node=0, edges_dict=edges_dict):
            return False
        if False in self.visited_all:
            return False
        return True
