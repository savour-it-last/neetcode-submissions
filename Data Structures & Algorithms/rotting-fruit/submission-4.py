class Solution:
    def makeRotten(self, grid: list[list[int]], row: int, col: int, q: list[int]) -> list[int]:
        """
        Make an adjacent fruit rotten
        """
        if (
            (row, col) in self.visited
            or row < 0
            or row == len(grid)
            or col < 0
            or col == len(grid[0])
            or grid[row][col] == 0
            or grid[row][col] == 2
        ):
            return q

        grid[row][col] = 2
        self.visited.add((row, col))
        q.append((row, col))
        return q

    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.visited = set()
        q = collections.deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    # push all rotten fruit locations to a queue
                    q.append((row, col))
                    self.visited.add((row, col))

        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                q = self.makeRotten(grid=grid, row=r + 1, col=c, q=q)
                q = self.makeRotten(grid=grid, row=r - 1, col=c, q=q)
                q = self.makeRotten(grid=grid, row=r, col=c + 1, q=q)
                q = self.makeRotten(grid=grid, row=r, col=c - 1, q=q)
            if q:
                time+=1
        for row in grid:
            if 1 in row:
                return -1
        return time
