class Solution:
    def island_checker_bfs(
        self, grid: list[list[str]], row: int, col: int, rows: int, cols: int, visited: set
    ) -> set:
        visited.add((row, col))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            if (
                (row + dr) in range(rows)
                and (col + dc) in range(cols)
                and grid[row + dr][col + dc] == "1"
                and (row + dr,col + dc) not in visited
            ):
                visited = self.island_checker_bfs(
                    grid=grid, row=row + dr, col=col + dc, rows=rows, cols=cols, visited=visited
                )
                    
        return visited

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    visited = self.island_checker_bfs(
                        grid=grid, row=r, col=c, rows=rows, cols=cols, visited=visited
                    )
                    islands += 1
        return islands
