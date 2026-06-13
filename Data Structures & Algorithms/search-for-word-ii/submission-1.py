class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endofword = False
        self.word = ""

class Solution:
    
    def __init__(self)->None:
        self.root = TrieNode()
        self.moves = [[-1, 0], [0,-1], [1, 0], [0,1] ]

    def addWordToTrie(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofword = True
        curr.word = word

    def dfs_trie(self, curr: TrieNode, row: int, col: int, board: list[list[str]])->None:
        if (row, col) in self.visited:
            return None
        char = board[row][col]
        if char not in curr.children:
            return None

        self.visited.add((row, col))
        
        curr = curr.children[char]
        
        if curr.endofword:
            self.found_words.add(curr.word)
        
        for move in self.moves:
            new_row = row + move[0]
            new_col = col + move[1]
            if (new_row >= 0 and new_row < len(board)) and (new_col >= 0 and new_col < len(board[0])):
                self.dfs_trie(curr=curr, row=new_row, col=new_col, board=board)

        self.visited.remove((row, col))
        return None    

    def findWords(
        self,
        board: List[List[str]],
        words: List[str],
    ) -> List[str]:

        found_words = []
        
        for word in words:
            self.addWordToTrie(word=word)
        
        self.visited = set()
        self.found_words = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.dfs_trie(curr=self.root, row=i, col=j, board=board)

        return list(self.found_words)