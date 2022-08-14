# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.ret = 0
        self.dfs(root, 1)
        return self.ret
    
    def dfs(self, root, depth):
        if root:
            if depth > self.ret:
                self. ret = depth
            self.dfs(root.left, depth + 1)
            self.dfs(root.right, depth + 1)
