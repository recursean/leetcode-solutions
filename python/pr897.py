# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        nodes = self.inorder(root, [])
        prev = None
        for node in nodes:
            if prev is not None:
                prev.right = node
            prev = node
        return nodes[0]
        
    def inorder(self, root: TreeNode, nodes=[]):
        if root is not None:
            nodes = self.inorder(root.left, nodes)
            root.left = None
            nodes.append(root)
            nodes = self.inorder(root.right, nodes)
            root.right = None
        return nodes
