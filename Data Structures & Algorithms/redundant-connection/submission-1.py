class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Iterate through the edges.
        # Each node belongs to a connected component.
        # If both nodes of an edge already belong to the same
        # component, adding that edge creates a cycle.

        connection_map = {}

        for n1, n2 in edges:
            if n1 not in connection_map:
                connection_map[n1] = n1

            if n2 not in connection_map:
                connection_map[n2] = n2

            root1 = self._find_root(connection_map, n1)
            root2 = self._find_root(connection_map, n2)

            if root1 == root2:
                return [n1, n2]

            self._join(connection_map, root1, root2)

        return []

    def _find_root(self, connection_map: dict[int, int], node: int) -> int:
        """Find the representative of the component containing a node."""
        while connection_map[node] != node:
            node = connection_map[node]

        return node

    def _join(
        self,
        connection_map: dict[int, int],
        root1: int,
        root2: int,
    ) -> None:
        """Join two different connected components."""
        connection_map[root2] = root1