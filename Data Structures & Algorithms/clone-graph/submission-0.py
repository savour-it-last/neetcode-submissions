"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = collections.deque()
        q.append(node)
        new_node = Node(val = node.val)
        root = new_node
        visited = {node: new_node}
        while q:
            node = q.popleft()
            clone = visited[node]
            if not node.neighbors:
                continue
            neighbor_list = []
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    new_neighbor = Node(val = neighbor.val)
                    visited[neighbor] = new_neighbor
                neighbor_list.append(visited[neighbor])
            clone.neighbors = neighbor_list   
        return root
        

