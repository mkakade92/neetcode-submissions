# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []

        def preorder(node):
            if node is None:
                s.append("#")
                return
            s.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return ",".join(s)
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals =data.split(",")
        self.i = 0

        def preorder():
            if vals[self.i]=='#':
                self.i+=1
                return None
            node =TreeNode(int(vals[self.i]))
            self.i+=1
            node.left = preorder()
            node.right = preorder()
            return node
        return preorder()

