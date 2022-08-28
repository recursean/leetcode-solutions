# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ret = []
        self.dfs(root, 0, targetSum, [])
        return self.ret
        
    def dfs(self, root, sum, tsum, path):
        if root is not None:
            path.append(root.val)
            if root.left is None and root.right is None:
                if sum + root.val == tsum:
                    self.ret.append(path.copy())
            else:
                self.dfs(root.left, sum + root.val, tsum, path)
                self.dfs(root.right, sum + root.val, tsum, path)
            path.pop()
