from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.d = set()
        return self.preorder(root,k)

    def preorder(self, root: Optional[TreeNode], k: int):
        if root is None:
            return False

        if k - root.val in self.d:
            return True

        self.d.add(root.val)
        if(self.preorder(root.left, k)):
            return True
        if(self.preorder(root.right, k)):
            return True

        return False

sol = Solution()
root = TreeNode(1)
k = 2
print(sol.findTarget(root,2))