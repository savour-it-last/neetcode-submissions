class Solution:
    def addRooms(self, grid: list[list[int]], row: int, col: int, q: list[tuple[int, int]])->list[tuple[int,int]]:
        for direction in self.directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if 0<=new_row<len(grid) and 0<=new_col<len(grid[0]) and grid[new_row][new_col] != 0 and grid[new_row][new_col] != -1 and (new_row,new_col) not in self.visited:
                self.visited.add((new_row,new_col))
                q.append((new_row, new_col))

        return q


    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.directions = [[1,0], [0,1], [-1,0], [0,-1]]
        q = collections.deque()
        self.visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    # Found a treasure
                    q.append((row, col))
                    self.visited.add((row,col))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] =dist
                q = self.addRooms(grid=grid, row=r, col=c, q=q)
            dist+=1

            