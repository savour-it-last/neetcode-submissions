class Solution:
    def traverse(self, grid: list[list[int]], row: int, col: int) -> int:
        count = 1
        self.visited.add((row,col))
        for direction in self.directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if new_row<len(grid) and new_row >= 0 and new_col < len(grid[0]) and new_col >= 0 and grid[new_row][new_col]==1 and (new_row, new_col) not in self.visited:
                count+=self.traverse(grid=grid, row=new_row, col=new_col)

        return count
        

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        self.directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in self.visited:
                    count = self.traverse(grid=grid, row=row, col=col)
                    res = max(res, count)
        return res
