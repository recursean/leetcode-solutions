# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ret = False
        self.dfs(root, 0, targetSum)
        return self.ret
    
    def dfs(self, root, sum, tsum):
        if root is not None:
            if root.left is None and root.right is None:
                if sum + root.val == tsum:
                    self.ret = True
            else:
                self.dfs(root.left, sum + root.val, tsum)
                self.dfs(root.right, sum + root.val, tsum)
