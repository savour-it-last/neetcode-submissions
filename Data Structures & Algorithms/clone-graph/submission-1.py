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
        root = Node(val=node.val)
        clone = root
        q = collections.deque()
        q.append(node)
        visited = {node: clone}
        while q:
            node = q.popleft()
            clone = visited[node]
            if not node.neighbors:
                continue
            curr_node_neighbor_list = []
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    neighbor_copy = Node(val=neighbor.val)
                    visited[neighbor] = neighbor_copy
                curr_node_neighbor_list.append(visited[neighbor])
            clone.neighbors = curr_node_neighbor_list
        return root
        
                
