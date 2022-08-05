# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root, [])
    
    def dfs(self, root, vals):
        if root is not None:
            vals = self.dfs(root.left, vals)
            vals = self.dfs(root.right, vals) 
            
            vals.append(root.val)
            
        return vals
