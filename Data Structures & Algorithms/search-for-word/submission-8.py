class Solution:
    def dfs(
        self, word: str, index: int, board: list[list[str]], row: int, col: int
    ) -> bool:


        if word[index] != board[row][col] or (row, col) in self.visited:
            return False

        if index == len(word)-1:
            return True
        
        self.visited.add((row, col))

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        found = False
        for direction in directions:
            dr = row + direction[0]
            dc = col + direction[1]
            if 0 <= dr < len(board) and 0 <= dc < len(board[0]):
                if self.dfs(word=word, index=index + 1, board=board, row=dr, col=dc):
                    found = True
                    break

        self.visited.remove((row, col))
        return found

    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.visited = set()
                if self.dfs(word=word, index=0, board=board, row=row, col=col):
                    return True
        return False
