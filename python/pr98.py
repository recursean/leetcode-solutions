# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('inf'), float('-inf'))
    
    def dfs(self, root, smaller, larger):
        if not root:
            return True
        if root.val <= larger or root.val >= smaller:
            return False
        return self.dfs(root.left, root.val, larger) and self.dfs(root.right, smaller, root.val)
