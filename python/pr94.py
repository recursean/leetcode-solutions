# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    nums = []
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.nums = []
        self.it(root)
        return self.nums
    
    def it(self, root):
        if root is None:
            return
        
        self.it(root.left)
        self.nums.append(root.val)
        self.it(root.right)
        
        return