class Solution:
    def can_traverse_2_oceans(
        self, heights: list[list[int]], curr_row: int, curr_col: int, max_row: int, max_col: int
    ) -> bool:
        omni_directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        q = collections.deque()
        q.append([curr_row, curr_col])
        visited = set()
        visited.add((curr_row, curr_col))
        atlantic_visited = False
        pacific_visited = False
        if curr_row == 0 or curr_col == 0:
            pacific_visited = True
        if curr_row == max_row - 1 or curr_col == max_col-1:
            atlantic_visited = True
        if atlantic_visited and pacific_visited:
            return True
        while q:
            curr_row, curr_col = q.popleft()
            for dr, dc in omni_directions:
                adj_r = curr_row + dr
                adj_c = curr_col + dc
                if (
                    adj_r in range(max_row)
                    and adj_c in range(max_col)
                    and heights[adj_r][adj_c] <= heights[curr_row][curr_col]
                    and (adj_r, adj_c) not in visited
                ):
                    visited.add((adj_r, adj_c))
                    q.append([adj_r, adj_c])
                    if adj_r == 0 or adj_c == 0:
                        pacific_visited = True
                    if adj_r == max_row - 1 or adj_c == max_col-1:
                        atlantic_visited = True
                    if atlantic_visited and pacific_visited:
                        return True
        return False

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Pacific ocean is in row = 0 or col = 0
        # Atlantic ocean is in row = row_count - 1 or col = col_count - 1

        # create loop to each cell.
        # each cell must be depth first searched so it reaches pacific and atlantic else false.
        row_count, col_count = len(heights), len(heights[0])
        res = []
        for row in range(row_count):
            for col in range(col_count):
                if self.can_traverse_2_oceans(
                    heights=heights, curr_row=row, curr_col=col, max_row=row_count, max_col=col_count
                ):
                    res.append([row, col])
        return res
