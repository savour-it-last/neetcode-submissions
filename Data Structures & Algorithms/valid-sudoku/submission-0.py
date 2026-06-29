class Solution:
    def _get_square_limiter(self, row: int, col: int) -> tuple[int, int]:
        if row <=2:
            row = 2
        elif row <=5:
            row = 5
        elif row <=8:
            row = 8
        
        if col <=2:
            col =2
        elif col<=5:
            col=5
        elif col <=8:
            col = 8
        
        return (row, col)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # To check column compliancy
        col_dict: dict[int, list[bool]] = {}
        for col in range(len(board[0])):
            col_dict[col] = [False]*9
        
        # To check 3*3 compliancy
        matrix_dict: dict[tuple[int, int], list[bool]] = {}
        for row_limiter in range(2, len(board), 3):
            for col_limiter in range(2, len(board[0]), 3):
                matrix_dict[(row_limiter, col_limiter)] = [False]*9

        # Main loop
        for row in range(len(board)):
            # To check row compliancy
            row_visited = [False]*9
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                # since its 1 to 9
                val = int(board[row][col]) - 1
                # either that row already visited this number or
                # that column already visited the number
                limiters = self._get_square_limiter(row=row, col=col)
                
                if row_visited[val] or col_dict[col][val] or matrix_dict[limiters][val]:
                    return False
                row_visited[val] = True
                col_dict[col][val] = True
                matrix_dict[limiters][val] = True
        
        return True
                