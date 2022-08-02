# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min = -1
        self.val = -1
        self.inorder(root)
        return self.min
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            if self.val != -1:
                val = abs(root.val - self.val)
                self.min = val if self.min == -1 or val < self.min else self.min
            self.val = root.val
            self.inorder(root.right)
