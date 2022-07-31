# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        nodes = []
        root = None
        for i,val in enumerate(preorder):
            nn = TreeNode(val)
            if i == 0:
                root = nn
            if nodes and val < nodes[len(nodes)-1].val:
                nodes[len(nodes)-1].left = nn
            else:
                p = None
                while nodes and val > nodes[len(nodes)-1].val:
                    p = nodes.pop()
                if p is not None:
                    p.right = nn
            nodes.append(nn)
        return root
