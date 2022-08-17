# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        self.dfs(root)
        return self.ret
        
    def dfs(self, root):
        if root is not None:
            ls, lc = self.dfs(root.left)
            rs, rc = self.dfs(root.right)
            
            sum = ls + rs + root.val
            childs = lc + rc + 1
            
            if sum // childs == root.val:
                self.ret += 1
                
            return sum, childs
        
        else:
            return 0, 0
            
