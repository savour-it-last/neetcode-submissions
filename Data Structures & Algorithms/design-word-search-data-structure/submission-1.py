class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endofword = True
    
    def dfs(self, ind: int, root: TrieNode, word: str)->bool:
        curr = root
        for i in range(ind, len(word)):
            c = word[i]
            if c == ".":
                for child in curr.children.values():
                    if self.dfs(ind = i + 1, root=child, word=word):
                        return True
                return False
            else:
                if c not in curr.children:
                    return False
                curr = curr.children[c]
        return curr.endofword

    def search(self, word: str) -> bool:
        return self.dfs(0, self.root, word)

        
