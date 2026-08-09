# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.MAXSUM =  -float('inf')
        
        def dfs(node):
            if node is None:
                return 

            left = self.getMax(node.left)
            right = self.getMax(node.right)
            self.MAXSUM = max(self.MAXSUM,node.val+left+right)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.MAXSUM

    def getMax(self,node):
        if not node:
            return 0
        lMax = self.getMax(node.left)
        rMax = self.getMax(node.right)
        return max(0,node.val+max(lMax,rMax))
