# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ret = -1
        self.inorder(root, k, 1)
        return self.ret
        
    def inorder(self, root, k, i):
        if root is not None and self.ret == -1:
            i = self.inorder(root.left, k, i)
            
            if k == i:
                self.ret = root.val
            i += 1
            
            i = self.inorder(root.right, k, i)
            
        return i 
