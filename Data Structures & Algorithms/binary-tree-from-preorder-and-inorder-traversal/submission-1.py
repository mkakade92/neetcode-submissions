# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        mp = {val:ind for ind,val in enumerate(inorder)}
        preInd = [0]
        return self.build(mp,preorder,preInd,0,len(inorder)-1)
        

    def build(self,mp,preorder,preInd,left,right):
        if left>right:
            return None
        
        rootVal = preorder[preInd[0]]
        preInd[0]+=1
        root = TreeNode(rootVal)
        index = mp[rootVal]
        root.left  = self.build(mp,preorder,preInd,left,index-1)
        root.right = self.build(mp,preorder,preInd,index+1,right)
        return root
            
            