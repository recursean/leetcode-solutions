# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.modes = {}
        self.traverse(root)
        ret = []
        max = 0
        for k,v in self.modes.items():
            if v == max:
                ret.append(k)
            elif v > max:
                ret = []
                ret.append(k)
                max = v
        return ret
    
    def traverse(self, root):
        if root is not None:
            self.traverse(root.left)
            if root.val in self.modes:
                self.modes[root.val] += 1
            else:
                self.modes[root.val] = 1
            self.traverse(root.right)
