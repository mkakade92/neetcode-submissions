
class Node:
    def __init__(self):
        self.children = [None]*26
        self.eow = False
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            
            ind = ord(c)-ord('a')
            if curr.children[ind] is None:
                curr.children[ind] = Node()
            curr = curr.children[ind]
        curr.eow = True
        

    def search(self, word: str) -> bool:
        
        return self._search(word,0,self.root)
    
    def _search(self,word,ind,node):
        
        if ind==len(word):
            return node.eow
        
        c = word[ind]

        if c=='.':

            for child in node.children:
                if child and self._search(word,ind+1,child):
                    return True
            return False
        else:
            i = ord(c) - ord('a')

            child = node.children[i]
            if child is None:
                return False
            return self._search(word,ind+1,child)
