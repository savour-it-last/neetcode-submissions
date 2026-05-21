class Solution:
    def find_ocean_reachable_cells(
        self, heights: list[list[int]], curr_row: int, curr_col: int, max_row: int, max_col: int
    ) -> set:
        omni_directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        reachable = set()
        q = collections.deque()
        q.append([curr_row, curr_col])
        visited = set()
        visited.add((curr_row, curr_col))
        reachable.add((curr_row, curr_col))
        while q:
            curr_row, curr_col = q.popleft()
            for dr, dc in omni_directions:
                adj_r = curr_row + dr
                adj_c = curr_col + dc
                if (
                    adj_r in range(max_row)
                    and adj_c in range(max_col)
                    and heights[adj_r][adj_c] >= heights[curr_row][curr_col]
                    and (adj_r, adj_c) not in visited
                ):
                    visited.add((adj_r, adj_c))
                    q.append([adj_r, adj_c])
                    reachable.add((adj_r, adj_c))
        return reachable

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Pacific ocean is in row = 0 or col = 0
        # Atlantic ocean is in row = row_count - 1 or col = col_count - 1

        # create loop to each cell.
        # each cell must be depth first searched so it reaches pacific and atlantic else false.
        row_count, col_count = len(heights), len(heights[0])
        res = []
        pacific_reachable = set()
        atlantic_reachable = set()
        for row in range(row_count):
            for col in range(col_count):
                if row == 0 or col == 0:
                    pacific_reachable |= self.find_ocean_reachable_cells(
                    heights=heights, curr_row=row, curr_col=col, max_row=row_count, max_col=col_count
                )
                if row == row_count-1 or col == col_count-1:
                    atlantic_reachable |= self.find_ocean_reachable_cells(
                    heights=heights, curr_row=row, curr_col=col, max_row=row_count, max_col=col_count
                )
        return list(pacific_reachable&atlantic_reachable)
