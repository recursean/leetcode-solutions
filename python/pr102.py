# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.ret = [[]]
        q = deque([root,0])
        c = 0
        while q:
            n = q.popleft()
            l = q.popleft()

            if l != c:
                self.ret.append([])
                c = l

            self.ret[c].append(n.val)
            
            if n.left:
                q.append(n.left)
                q.append(l+1)
            if n.right:
                q.append(n.right)
                q.append(l+1)
        
        return self.ret
