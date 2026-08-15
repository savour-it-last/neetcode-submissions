class Solution:
    def markEdgeConnected(self, board: list[list[str]], r: int, c: int) -> None:
        """
        Marks all ok ones, ie connected to edge
        """
        self.edgeConnected.add((r, c))
        for direction in self.directions:
            new_row = r + direction[0]
            new_col = c + direction[1]
            if (
                0 <= new_row < len(board)
                and 0 <= new_col < len(board[0])
                and (new_row, new_col) not in self.edgeConnected
                and board[new_row][new_col] == "O"
            ):
                self.markEdgeConnected(board=board, r=new_row, c=new_col)

    def solve(self, board: List[List[str]]) -> None:
        self.edgeConnected = set()
        self.directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        max_c = len(board[0])
        max_r = len(board)
        # alternative cause anyway they will be visited if adjacent
        for i in range(0, max_r):
            if board[i][0] == "O":
                self.markEdgeConnected(board=board, r=i, c=0)

            if board[i][max_c - 1] == "O":
                self.markEdgeConnected(board=board, r=i, c=max_c - 1)

        for i in range(0, max_c):
            if board[0][i] == "O":
                self.markEdgeConnected(board=board, r=0, c=i)

            if board[max_r - 1][i] == "O":
                self.markEdgeConnected(board=board, r=max_r - 1, c=i)

        for row in range(max_r):
            for col in range(max_c):
                if (row, col) not in self.edgeConnected and board[row][col] == "O":
                    board[row][col] = "X"
