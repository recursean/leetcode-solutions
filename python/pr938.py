# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.inorder(root, low, high, 0)
    def inorder(self, root: TreeNode, low: int, high: int, sum: int) -> int:
        if root is not None:
            if root.val >= low and root.val <= high:
                sum += root.val
            sum = self.inorder(root.left, low, high, sum)
            sum = self.inorder(root.right, low, high, sum)
        return sum
