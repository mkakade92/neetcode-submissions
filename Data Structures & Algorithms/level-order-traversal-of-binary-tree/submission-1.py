# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        li = []

        while q:
            tLi = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    tLi.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if tLi:
                li.append(tLi)
        return li


