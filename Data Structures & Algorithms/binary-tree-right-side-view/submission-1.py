# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q  = deque()

        res = []

        
        q.append(root)

        while q:
            curr_level = []
            level_size = len(q)
            
            for i in range(level_size):
                node = q.popleft()

                curr_level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(curr_level[-1])
        return res
            
            

            

        
        