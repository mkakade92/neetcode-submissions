class Node:
    def __init__(self):
        self.eow = False
        self.children=[None]*26

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        #iterate over string
        root = self.root
        for c in word:
            #try adding c to tree
            index  = ord(c) - ord('a')
            if root.children[index] is None:
                root.children[index] = Node()
            root = root.children[index]
        
        root.eow = True


    def search(self, word: str) -> bool:

        root = self.root

        for c in word:

            index =  ord(c) - ord('a')
            if root.children[index] is None:
                return False
            root = root.children[index]
        return root.eow
        

    def startsWith(self, prefix: str) -> bool:

        root = self.root

        for c in prefix:
            index = ord(c) - ord('a')
            if root.children[index] is None:
                return False
            root = root.children[index]
        return True
        
        