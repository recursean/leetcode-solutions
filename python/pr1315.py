# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum = 0
        self.dfs(root, False, False)
        return self.sum
        
    def dfs(self, root, pEv, gpEv):
        if root:
            if gpEv:
                self.sum += root.val
                
            ev = True if root.val % 2 == 0 else False
            
            self.dfs(root.left, ev, pEv)
            self.dfs(root.right, ev, pEv)
