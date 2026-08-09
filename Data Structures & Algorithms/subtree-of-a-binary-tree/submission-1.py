# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and subRoot:
            return self.isSimilar(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        return False
                
    def isSimilar(self,p,q):

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q1:
            for _ in range(len(q1)):
                node_p = q1.popleft()
                node_q = q2.popleft()
                
                if node_p is None and node_q is None:
                    continue
                
                if node_p is None or node_q is None or node_p.val!=node_q.val:
                    return False
                
                q1.append(node_p.left)
                q1.append(node_p.right)
                q2.append(node_q.left)
                q2.append(node_q.right)
        return True
