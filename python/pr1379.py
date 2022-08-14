# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.ret = None
        self.dfs(cloned, target.val)
        return self.ret
    
    def dfs(self, root, target):
        if root is not None and self.ret is None:
            if root.val == target:
                self.ret = root
                return
            self.dfs(root.left, target)
            self.dfs(root.right, target)
