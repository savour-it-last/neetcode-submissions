class Solution:
    def traverse_from_node(self, node: int, link_dict: list[set[int]])->None:
        if self.visited[node]:
            return None

        self.visited[node] = True

        for edge_node in link_dict[node]:
            if edge_node == node:
                continue
            self.traverse_from_node(node=edge_node, link_dict=link_dict)

        return None


    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        link_dict = {i: set() for i in range(n)}
        self.visited = [False for i in range(n)]
        component_count = 0

        for edge in edges:
            link_dict[edge[0]].add(edge[1])
            link_dict[edge[1]].add(edge[0])

        for i in range(n):
            if not self.visited[i]:
                self.traverse_from_node(node=i, link_dict=link_dict)
                component_count+=1
        
        return component_count
            
