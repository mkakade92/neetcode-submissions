class Node:
    def __init__(self):
        self.children = [None]*26
        self.word = None
    
class Trie:
    def __init__(self):
        self.root = Node()

    def add(self,word):
        curr = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if curr.children[ind] is None:
                curr.children[ind] = Node()
            curr = curr.children[ind]
        curr.word = word

class Solution:
   def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)

        r = len(board)
        c = len(board[0])
        res = set()

        def dfs(i, j, curr_node):
            char = board[i][j]
            ind = ord(char) - ord('a')
            next_node = curr_node.children[ind]
            
            if not next_node:
                return

            if next_node.word:
                res.add(next_node.word)
                next_node.word = None # Optimization: avoid duplicates and redundant searches

            board[i][j] = '#'
            for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ni, nj = i + x, j + y
                if 0 <= ni < r and 0 <= nj < c and board[ni][nj] != '#':
                    dfs(ni, nj, next_node)
            board[i][j] = char

        for i in range(r):
            for j in range(c):
                dfs(i, j, trie.root)
        return list(res)